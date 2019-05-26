
module sar(clk, cmp, eoc, out);
	input clk;
	input cmp;
		
	output eoc;
	output [7:0]out;
	
	reg [7:0]a = 0;
	reg [7:0]b = 255;
	
	reg [3:0]step = 0;
	
	assign out = (b-a)/2+a;
	assign eoc = (step == 9);
	
	always @(posedge clk) begin
		if (cmp) begin
			a <= (b-a)/2+a;
		end else begin
			b <= (b-a)/2+a;
		end
		if (step < 9) begin
			step <= step + 1;
		end else begin
			a <= 0;
			b <= 255;
			step <= 0;
		end
		
	end
	

endmodule