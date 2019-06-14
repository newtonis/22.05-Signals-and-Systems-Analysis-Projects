module rochi_start(clk1, clk2, out);
	input clk1;
	input clk2;
	
	output out;
	
	reg [20:0]counter = 0;
	reg last_clk2 = 0;
	
	assign out = (counter > 400 && counter < 480);
	
	always @(posedge clk1) begin
		if (clk2 == 1 && last_clk2 == 0) begin
			counter <= 0;
		end else if (counter < 1000) begin
			counter <= counter + 1;
		end else begin
			counter <= 1000;
		end
		
		last_clk2 <= clk2;
	end
endmodule