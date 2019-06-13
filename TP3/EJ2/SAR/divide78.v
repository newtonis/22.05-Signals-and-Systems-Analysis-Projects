module divide78(in, out);
	input in;
	output out;
	
	reg [24:0]cnt = 0;
	assign out = cnt < 39; //78
	
	always @(posedge in) begin
		if (cnt < 39*2) begin
			cnt <= cnt + 1;
		end else begin
			cnt <= 0;
		end
		
	end
	
endmodule