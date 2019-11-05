"Custom argument handler types for Click"

import click
import json
from pathlib import Path
from contextlib import contextmanager
from grpclib.client import Channel, GRPCError
from tabulate import tabulate
from xml.etree import ElementTree as xml

from porerefiner.protocols.porerefiner.rpc.porerefiner_grpc import PoreRefinerStub

#these two functions are hooks in case we decide to store only relative paths.
#paths going into the database will be relativized; paths going out will be
#absolutized.
#Whatever they do, they need to invert each other
def relativize_path(path):
    if isinstance(path, str):
        return Path(path)
    return path

def absolutize_path(path):
    if hasattr(path, '__fspath__'):
        return str(path)
    return path

class RunID:
    "can be either a string name or a numeric id"

    RUN_NAME = 'RUN_NAME'
    RUN_ID = 'RUN_ID'

    def __init__(self, the_value):
        if isinstance(the_value, str):
            self.val_type = RUN_NAME
        elif isinstance(the_value, int):
            self.val_type = RUN_ID
        else:
            raise ValueError("value must be str or int")



class ValidRunID(click.ParamType):

    def convert(self, value, param, ctx):
        try:
            return RunID(int(value))
        except ValueError:
            return RunID(value)

VALID_RUN_ID = ValidRunID()


# Channel context manager for CLI utils

@contextmanager
def server():
    from porerefiner.config import config
    channel = Channel(path=config['server']['socket'], ssl=config['server']['use_ssl'])
    client = PoreRefinerStub(channel)
    try:
        yield client
    except GRPCError as e:
        raise
    finally:
        channel.close()

#formatters for run output

@contextmanager
def hr_formatter(extend=False):
    rec = []
    def print_run(run):
        rec.append(dict(id=run.id,
                        name=run.name,
                        nickname=run.nickname,
                        status=run.status,
                        samples=len(run.samples),
                        files=sum([len(sam.files) for sam in run.samples]),
                        tags=",".join(run.tags)))
        if extend:
            for sample in run.samples:
                rec.append(dict(id=sample.id,
                                name=sample.name,
                                nickname=sample.accession,
                                barcode_id=sample.barcode_id,
                                organism=sample.organism,
                                comment=sample.comment,
                                user=sample.user,
                                files=len(sample.files),
                                tags=",".join(sample.tags)))
    yield print_run
    print(tabulate(rec, headers="keys"))

@contextmanager
def json_formatter(extend=False):
    rec = []
    def print_run(run):
        rec.append(run)
    yield print_run
    print(json.dumps(rec))

@contextmanager
def xml_formatter(extend=False):
    rec = []
    def print_run(run):
        rec.append(run)
    yield print_run
    print(xml.toString())
