# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: porerefiner/protocols/porerefiner/rpc/porerefiner.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.timestamp_pb2
import google.protobuf.duration_pb2
import porerefiner.protocols.porerefiner.rpc.porerefiner_pb2


class PoreRefinerBase(abc.ABC):

    @abc.abstractmethod
    async def GetRuns(self, stream: 'grpclib.server.Stream[porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunListRequest, porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunListResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRunInfo(self, stream: 'grpclib.server.Stream[porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunRequest, porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AttachSheetToRun(self, stream: 'grpclib.server.Stream[porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunAttachRequest, porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.GenericResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RsyncRunTo(self, stream: 'grpclib.server.Stream[porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunRsyncRequest, porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunRsyncResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Tag(self, stream: 'grpclib.server.Stream[porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.TagRequest, porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.GenericResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/porerefiner.rpc.PoreRefiner/GetRuns': grpclib.const.Handler(
                self.GetRuns,
                grpclib.const.Cardinality.UNARY_UNARY,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunListRequest,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunListResponse,
            ),
            '/porerefiner.rpc.PoreRefiner/GetRunInfo': grpclib.const.Handler(
                self.GetRunInfo,
                grpclib.const.Cardinality.UNARY_UNARY,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunRequest,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunResponse,
            ),
            '/porerefiner.rpc.PoreRefiner/AttachSheetToRun': grpclib.const.Handler(
                self.AttachSheetToRun,
                grpclib.const.Cardinality.UNARY_UNARY,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunAttachRequest,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.GenericResponse,
            ),
            '/porerefiner.rpc.PoreRefiner/RsyncRunTo': grpclib.const.Handler(
                self.RsyncRunTo,
                grpclib.const.Cardinality.UNARY_UNARY,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunRsyncRequest,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunRsyncResponse,
            ),
            '/porerefiner.rpc.PoreRefiner/Tag': grpclib.const.Handler(
                self.Tag,
                grpclib.const.Cardinality.UNARY_UNARY,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.TagRequest,
                porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.GenericResponse,
            ),
        }


class PoreRefinerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetRuns = grpclib.client.UnaryUnaryMethod(
            channel,
            '/porerefiner.rpc.PoreRefiner/GetRuns',
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunListRequest,
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunListResponse,
        )
        self.GetRunInfo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/porerefiner.rpc.PoreRefiner/GetRunInfo',
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunRequest,
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunResponse,
        )
        self.AttachSheetToRun = grpclib.client.UnaryUnaryMethod(
            channel,
            '/porerefiner.rpc.PoreRefiner/AttachSheetToRun',
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunAttachRequest,
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.GenericResponse,
        )
        self.RsyncRunTo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/porerefiner.rpc.PoreRefiner/RsyncRunTo',
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunRsyncRequest,
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.RunRsyncResponse,
        )
        self.Tag = grpclib.client.UnaryUnaryMethod(
            channel,
            '/porerefiner.rpc.PoreRefiner/Tag',
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.TagRequest,
            porerefiner.protocols.porerefiner.rpc.porerefiner_pb2.GenericResponse,
        )
