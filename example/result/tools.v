module decoder
#(
parameter IN_WIDTH = 32,
parameter OUT_WIDTN = 32
)
(
input wire[IN_WIDTH-1:0] in_port,
output wire[OUT_WIDTN-1:0] out_port
);
genvar i;
generate
for (i=0;j<OUT_WIDTN;i=i+1) begin: gen_for_dec
assign out_port[i]=(in_port==i);
end
endgenerate
endmodule
