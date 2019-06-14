module latch_sync(clk50, clk, eoc, out);
	input clk, eoc, clk50;
	reg last_clk = 0;
	reg last_eoc = 0;
	reg flag = 0;
	
	output out;
	reg [20:0] counter = 0;
	
	assign out = !(counter == 0 && flag == 0);
	
	always @(posedge clk50) begin
	
		if (out == 1 && last_clk == 0 && clk == 1) begin
			counter <= 100;
			flag <= 0;
		end else if (counter > 0) begin
			counter <= counter - 1;	
		end
		if (out == 0 && last_eoc == 0 && eoc == 1) begin
			flag <= 1;
		end
		last_clk <= clk;
		last_eoc <= eoc;
		
	end
endmodule