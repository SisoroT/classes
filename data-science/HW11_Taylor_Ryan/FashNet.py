import torch
import torch.nn as nn
import torch.nn.functional as F


class FashNet(nn.Module):
    def __init__(self, in_d, out_d):
        super(FashNet, self).__init__()

        # Create three fully-connected Linear layers: 256, 128, and 64 nodes wide
        # Follow each with a ReLU activation layer
        ## Your code here

        # Create the last fully-connected Linear layer that takes it down to out_d nodes

        # Create a softmax layer to create probabilities for each class

    # This is the method called when the model is doing inference
    def forward(self, x):

        # Run it through the three linear layers and their activation layers
        ## Your code here


        # Last layer and softmax
        ## Your code here

        return ## Your code here
