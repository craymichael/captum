#!/usr/bin/env python3

# pyre-strict
import torch.nn as nn


class Addition_Module(nn.Module):
    """Custom addition module that uses multiple inputs to assure correct relevance
    propagation. Any addition in a forward function needs to be replaced with the
    module before using LRP."""

    def __init__(self) -> None:
        super().__init__()

    # pyre-fixme[3]: Return type must be annotated.
    # pyre-fixme[2]: Parameter must be annotated.
    def forward(self, x1, x2):
        return x1 + x2
