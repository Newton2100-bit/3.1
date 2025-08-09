import typing


def foo(seq: typing.Sequence[str]) -> None:
    pass


# foo({'1','2','3'})
foo(["1", "2", "3"])
