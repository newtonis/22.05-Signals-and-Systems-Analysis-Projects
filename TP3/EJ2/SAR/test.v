module reloj(rst, ss, clk, ms, sec,min ,hs);
	input clk;
	input rst;
	input ss;
	
	output reg [14:0] ms = 0;
	output reg [6:0] sec = 0;
	output reg [6:0] min = 0;
	output reg [6:0] hs = 0;
	reg advance = 0;
	reg ss_old = 0; // start/stop
	reg rst_old = 0;
	
	always @(posedge clk) begin
		if (ss == 0 && ss_old == 1) begin // start/stop button falling edge
			advance <= !advance;
			
		end else if (rst == 1 && rst_old == 0) begin // reset button rising edge
			ms <= 0;
			sec <= 0;
			min <= 0;
			hs <= 0;
			advance <= 0;
		end else begin
			if (advance) begin
				if (ms < 9999) begin
					ms <= ms + 1;
				end else begin
					ms <= 0;
					if (sec < 59) begin
						sec <= sec + 1;
					end else begin
						sec <= 0;
						if (min < 59) begin
							min <= min + 1;
						end else begin
							min <= 0;
							if (hs < 23) begin
								hs <= hs + 1;
							end else begin
								hs <= 0;
							end
						end
					end
				end
			end
		end
		ss_old <= ss;
		rst_old <= rst;
	end
endmodule
