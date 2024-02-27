import struct
from torch import Tensor



def save_tensor(x: Tensor, data_path, filename):
    with open(data_path + filename, "wb") as fp:
        flattened_tensor = x.flatten()
        for date in flattened_tensor:
            fp.write(struct.pack("f", date.item()))
    print("data written to", data_path + filename)