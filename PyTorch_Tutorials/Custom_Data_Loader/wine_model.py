from wine_data_loader import dataloader
import torch
import torch.nn as nn
import torch.optim as optim

## Wine model
class NN(nn.Module):
    # Nn for wine dataset
    def __init__(self, input_size, num_classes):
        ## NN - input size = 11 , num_classes = 6 [3, 4, 5, 6, 7, 8]
        #  for wine data
        ## ADDITIONAL - can map classes to [0, 1, 2, 3, 4]
        super(NN, self).__init__()
        ## define your layers here
        ## Layers are linear, conv2d etc. For activations, use forward
        self.fc1 = nn.Linear(in_features=input_size, out_features=50)
        self.activation1 = nn.ReLU() ## Relu is in nn only
        self.fc2 = nn.Linear(in_features=50, out_features=num_classes)

    def forward(self, x):
        # Forward pass - IMPORTANT
        # Input x
        x = self.fc1(x)
        x = self.activation1(x)
        x = self.fc2(x)
        return x


# ###### -- Unit Test----------------------------------
# model = NN(11, 6)
# # Random dimensions, (batch_size, number_features)
# x = torch.randn(4, 11)
# ## Detach - remove from computation graph,
# #  otherwise keep tracking
# print(model(x)[0]) 
#  ## We want to return [4, 6]; 4 - for each sample, 
#  # 6 - for probability in each class
#  ### Shape is correct
# ####--------------------------------------------------

# SET DEVICE (GPU/CPU)
device = ('cuda' if torch.cuda.is_available() else 'cpu')

# Hyperparameters
input_size = 11
num_classes = 6
learning_rate = 0.001
num_epochs = 10

## We will split the batch internally, 3 for train, 1 for val
model = NN(input_size=input_size, num_classes=num_classes)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# train
for epoch in range(num_epochs):
    #  one epoch - seen all data points
    loss = None
    for batch_idx, (data, target) in enumerate(dataloader):
        # NO VALIDATION, OVERFITTING!
        train_data, train_target = data, target

        # forward
        train_preds = model(train_data.float())
        # print(train_preds)
        # print()
        # print(train_target)
        loss = criterion(train_preds, train_target.long())

        # backward
        optimizer.zero_grad()  ## Set all grad to 0
        loss.backward()

        ## GD
        optimizer.step()

    print(f"({epoch}) : Cross Entropy Loss = {loss.detach()}")


# Too much loss due to imbalance