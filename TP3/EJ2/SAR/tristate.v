module tristate(oe,in,out);
	input oe;
	input [7:0]in;
	output [7:0]out ;
	
	assign out = oe? in : 'bz;
endmodule