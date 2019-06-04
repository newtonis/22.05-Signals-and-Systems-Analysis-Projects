module mux8(in1, in2, control, out);
	input control;
	
	input [7:0]in1;
	input [7:0]in2;
	output [7:0]out;
	
	assign out = control ? in2 : in1;
	
endmodule