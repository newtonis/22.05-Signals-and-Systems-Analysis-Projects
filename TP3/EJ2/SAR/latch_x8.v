
module latch_x8(in, out, clk);
	input [7:0]in;
	output reg [7:0]out = 0;
	input clk;
	
	always @(posedge clk) begin
		out <= in;
	end
	
endmodule