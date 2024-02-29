import struct
from torch import Tensor



def save_tensor(x: Tensor, data_path, filename):
    with open(data_path + filename, "wb") as fp:
        flattened_tensor = x.flatten()
        for date in flattened_tensor:
            fp.write(struct.pack("f", date.item()))
    print("data written to", data_path + filename)
    
def save_tensor_to_hpp(x: Tensor, array_name: str, data_path, filename):
    x_flat = x.flatten()
    arr_len = int(list(x_flat.shape)[0])
    header_text_top = "#ifndef MVIT_{}\n".format(array_name.upper())
    header_text_top += "#define MVIT_{}\n\n".format(array_name.upper())
    header_text_top += "{}[{}] = {{\n".format(array_name, arr_len)
    
    with open(data_path + filename, "wt") as fp:
        cnt = 1
        fp.write(header_text_top)
        
        for date in x_flat:
            if cnt % 5 == 0:
                fp.write("\n")
            fp.write("{}, ".format(date.item()))
            cnt += 1
            
        fp.write("\n}\n\n#endif")