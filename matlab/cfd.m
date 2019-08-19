sample = -2:-1:-63;
h = double(2.^sample);
e = double(exp(1));
x = double(4);
fx = double(e^x/(x^4 + x^2 + 1));
x_add_h = x + h;
x_sub_h = x - h;
fxh = double(e.^x_add_h./(x_add_h.^4+x_add_h.^2+1));
fxmh = double(e.^x_sub_h./(x_sub_h.^4+x_sub_h.^2+1));
fd_approximation = double((fxh - fx)./h);
cd_approximation = double(fxh - fxmh)./(2*h);
actual_derivative = double(((x^4-4*x^3+x^2-2*x+1)*e^x)/(x^4+x^2+1)^2);
fd_error = double(abs(fd_approximation - actual_derivative)/abs(actual_derivative)); 
cd_error = double(abs(cd_approximation - actual_derivative)/abs(actual_derivative)); 
c_x_add_h = complex(x, h);
c_fx = double(complex(e.^c_x_add_h./(c_x_add_h.^4+c_x_add_h.^2+1)));
cfd_approximation = double(imag(c_fx))./h;
cfd_error = double(abs(cfd_approximation - actual_derivative)/abs(actual_derivative));

cd_error = cd_error';
fd_error = fd_error';
cfd_error = cfd_error';
sample = sample';

