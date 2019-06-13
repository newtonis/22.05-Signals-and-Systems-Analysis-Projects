
module modulador_delta(clk, cmp, eoc, out);
	input clk;
	input cmp;
	output eoc;
	output reg [7:0]out = 127;
	
	
//	assign eoc = clk;
	always @(posedge clk) begin
		
		//if (cmp) begin 
		//	out <= 50;
		//end else begin
		//	out <= 0;
		//end
		//out <= out + 1;
		if (cmp) begin // 
			if (out < 255) begin
				out <= out + 1;
			end else begin
				out <= 255;
			end
		end else begin
			if (out > 0) begin
				out <= out - 1;
			end else begin
				out <= 0;
			end
		end
	end
	
endmodule