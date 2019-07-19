module clock_divider16(clk_in, clk_out, period);
	input clk_in;
	output clk_out;
	input [40:0]period;
	reg [40:0]counter = 0;
	
	assign clk_out = counter >= (period/16)/2;
	
	always @(posedge clk_in) begin
		if (counter >= period/16) begin
			counter <= 0;
		end else begin
			counter <= counter + 1;
		end
	end
	
endmodule