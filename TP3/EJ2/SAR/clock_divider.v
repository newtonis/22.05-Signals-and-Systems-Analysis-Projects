module clock_divider(clk_in, clk_out, period);
	input clk_in;
	output clk_out;
	input [30:0]period;
	reg [30:0]counter = 0;
	
	assign clk_out = counter >= period/2;
	
	always @(posedge clk_in) begin
		if (counter == period) begin
			counter <= 0;
		end else begin
			counter <= counter + 1;
		end
	end
	
endmodule