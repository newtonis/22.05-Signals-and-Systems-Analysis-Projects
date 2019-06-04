module counter(clk, in, out);
	reg [7:0]value=0;
	input in;
	
	always (@posedge clk) begin
		if (in) begin
			value <= value + 1;
		end else begin
			value <= value - 1;
			
		end
	end
endmodule