module decoder
#(
  parameter IN_WIDTH,
  parameter OUT_WIDTN
)
(
    input  wire [IN_WIDTH - 1:0] in,
    output wire [OUT_WIDTN - 1:0] out
);
genvar i;
generate
for (i=0; i<OUT_WIDTN; i=i+1) begin: gen_for_dec
    assign out[i] = (in == i);
end
endgenerate


endmodule


