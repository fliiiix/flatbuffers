from __future__ import annotations

import flatbuffers
import numpy as np

import flatbuffers
import typing
from MyGame.Example.NestedUnion.Test import Test

uoffset: typing.TypeAlias = flatbuffers.number_types.UOffsetTFlags.py_type

class Test(object):
  @classmethod
  def SizeOf(cls) -> int: ...

  def Init(self, buf: bytes, pos: int) -> None: ...
  def A(self) -> int: ...
  def B(self) -> int: ...
class TestT(object):
  a: int
  b: int
  @classmethod
  def InitFromBuf(cls, buf: bytes, pos: int) -> TestT: ...
  @classmethod
  def InitFromPackedBuf(cls, buf: bytes, pos: int = 0) -> TestT: ...
  @classmethod
  def InitFromObj(cls, test: Test) -> TestT: ...
  def _UnPack(self, test: Test) -> None: ...
  def Pack(self, builder: flatbuffers.Builder) -> None: ...

def CreateTest(builder: flatbuffers.Builder, a: int, b: int) -> uoffset: ...

__all__ = ["Test","TestT",]

