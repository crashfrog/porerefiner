import yaml
from pathlib import Path
from os import environ
import logging

#from porerefiner.notifiers import REGISTRY, NOTIFIERS
import porerefiner.notifiers as notifiers
import porerefiner.jobs as jobs
import porerefiner.jobs.submitters as submitters

config_file = Path(environ.get('POREREFINER_CONFIG', '/Users/justin.payne/.porerefiner/config.yml'))


#Logging
log = logging.getLogger('porerefiner.config')

try:
    with open(config_file, 'r') as conf:
        config = yaml.safe_load(conf)
    log.info(f"Config file loaded from {config_file}")

except OSError:
    log.warning(f'No config file at {config_file}, creating...')
    from collections import defaultdict
    tree = lambda: defaultdict(tree) #this is a trick for defining a recursive defaultdict
    defaults = tree()
    defaults['porerefiner']['log_level'] = logging.INFO
    defaults['porerefiner']['run_polling_interval'] = 600
    defaults['porerefiner']['job_polling_interval'] = 1800
    defaults['database']['path'] = '/Users/justin.payne/.porerefiner/database.db'
    defaults['database']['pragmas']['foreign_keys'] = 1
    defaults['database']['pragmas']['journal_mode'] = 'wal'
    defaults['database']['pragmas']['cache_size'] = 1000
    defaults['database']['pragmas']['ignore_check_constraints'] = 0
    defaults['database']['pragmas']['synchronous'] = 0
    defaults['server']['socket'] = '/Users/justin.payne/.porerefiner/socket'
    defaults['server']['use_ssl'] = False
    defaults['nanopore']['path'] = '/Users/justin.payne/nanop'
    defaults['nanopore']['api'] = "localhost:9501"

    defaults['notifiers'] = [{'class':'ToastNotifier', 'config':dict(name='Default notifier', max=3)}]

    defaults['submitters'] = [{'class':'HpcSubmitter', 'config':dict()}]

    defaults['jobs'] = [{'class':'GuppyJob', 'config':dict(num_cores=16)}]

    def c(d):
        "Recursively convert this defaultdict to a dict"
        if isinstance(d, defaultdict):
            return {k:c(v) for k,v in d.items()}
        else:
            return d

    defaults = c(defaults)

    # defaults['']['']
    with open(config_file, 'w') as conf:
        yaml.dump(defaults, conf)

    config = defaults

except yaml.YAMLError as e:
    log.error(f"Couldn't read config file at {config_file}, error was:")
    log.error(e)
    quit(1)


#Socket
config['server']['socket'] = Path(environ.get('POREREFINER_SOCK', config['server']['socket']))
log.info(f"PoreRefiner socket at {config['server']['socket']}")

#Notifiers
log.info("Loading notifiers...")
for notifier_config in config.get('notifiers', []):
    log.info(f"Found notifier {notifier_config['config']['name']}")
    notifiers.REGISTRY[notifier_config['class']](**notifier_config['config'])
    #NOTIFIERS.append(notifier)

#Submitters
submitters.SUBMITTER = None
log.info("Loading job submitters...")
for submitter_config in config.get('submitters', []):
    log.info(f"Found submitter {submitter_config['class']}")
    submitters.REGISTRY[submitter_config['class']](**submitter_config['config'])

#Jobs
log.info("Loading jobs...")
for job_config in config.get('jobs', []):
    log.info(f"Found job {job_config['class']}")
    jobs.REGISTRY[job_config['class']](**job_config['config'])

def add_notifier_stub(notifier_cls):
    cp = config.copy() #we don't want the stub to actually take effect until reload
    cp['notifiers'].append(notifier_cls.toStub())
    with open(config_file, 'w') as conf:
        yaml.dump(cp, conf)


