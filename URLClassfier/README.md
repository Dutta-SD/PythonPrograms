# URL classifier
### By Sandip Dutta

---
## Overview

The function defined in url classifier takes in a url as input. 

It uses the **whoisxml** api for classifying into number of classes. To keep the function general, the function returns the following:

* a `list of tuples`, giving predictions and confidence score. Instead of returning 4 classes, this [any class among those defined by the API](https://website-categorization.whoisxmlapi.com/api/documentation/categories). 

This makes the function more general.

We also provide unit tests for verifying the function.

## Example
```python
>>> from url_classify import *
>>> get_url_prediction("bbc.com")
[('Television', 0.5820464358020851),   ('Holiday TV', 0.6636296385021508)]