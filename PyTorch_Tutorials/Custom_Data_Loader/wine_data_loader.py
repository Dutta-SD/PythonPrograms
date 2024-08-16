# Implementation of Custom Data Loader
# From Youtube, Python Engineer
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


### Custom Data Loader
class WineDataset(Dataset):

    def __init__(self):
        # Data Loading
        # Step  : 1 -> Load the data
        # Load in separate file, then keep only x and y
        # portions in selfP
        xy = np.loadtxt(
            './wine.csv',
            delimiter=",",
            skiprows=1)
        self.x = torch.from_numpy(xy[:, : -1])  # Last column is the target
        self.y = torch.tensor(xy[:, -1])  ## All the other columns
        self.n_samples = xy.shape[0]
        print(self.x.dtype, self.y.dtype)

    def __getitem__(self, index):
        # Dataset[0], say
        return (self.x[index], self.y[index])

    def __len__(self):
        # len(dataset)
        return self.n_samples


##### YAYYYYY!!!!!!!!!!!!!!!111 It is working
# Now we need to implement Data Loader
### Dataset - one sample
### Now this is a data generator, for whole dataset
#  once with 4 random samples
_dataset = WineDataset()
dataloader = DataLoader(
    dataset=_dataset,
    batch_size=4,
    shuffle=True,
    num_workers=2,
)
