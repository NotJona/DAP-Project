NewFile
import torch

# Annahme: self.weight und self.bias sind Tensor-Objekte

weight_type = type(self.weight)
bias_type = type(self.bias)

print("Typ von self.weight:", weight_type)
print("Typ von self.bias:", bias_type)