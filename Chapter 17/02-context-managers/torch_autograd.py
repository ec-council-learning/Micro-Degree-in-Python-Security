import torch


x = torch.tensor(1.0, requires_grad=True)
print(f'x autograd: {x.requires_grad}')
y = x * 3
print(f'y autograd: {y.requires_grad}')

with torch.no_grad():
    z = x * 3
    print(f'z autograd: {z.requires_grad}')
