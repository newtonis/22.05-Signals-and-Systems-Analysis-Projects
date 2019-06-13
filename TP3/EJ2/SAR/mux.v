module mux(in1, in2, control, out);
	input in1;
	input in2;
	input control;
	output out;
	assign out = control ? in1 : in2;
endmodule