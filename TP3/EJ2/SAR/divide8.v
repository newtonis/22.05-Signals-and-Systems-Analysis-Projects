module divide8(in, out);
	input in;
	output out;
	
	reg [4:0]cnt = 0;
	assign out = (cnt==9);
	always @(posedge in) begin
		if (cnt < 9) begin
			cnt <= cnt + 1;
		end else begin
			cnt <= 0;
		end
	end
endmodule