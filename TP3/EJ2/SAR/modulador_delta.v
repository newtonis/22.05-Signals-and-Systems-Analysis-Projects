
module modulador_delta(clk, cmp, eoc, out);
	input clk;
	input cmp;
	output eoc;
	output reg [7:0]out = 0;
	
	always @(posedge clk) begin
		if (cmp) begin
			out <= out + 1;
		end else begin
			out <= out - 1;
		end
	end
	
endmodule