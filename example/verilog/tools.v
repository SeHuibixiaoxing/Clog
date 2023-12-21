module decoder
#(
  parameter IN_WIDTH=5,
  parameter OUT_WIDTN=32
)
(
    input  [IN_WIDTH - 1:0] in,
    output [OUT_WIDTN - 1:0] out
);
genvar i;
generate for (i=0; i<OUT_WIDTN; i=i+1) begin: gen_for_dec
    assign out[i] = (in == i);
end endgenerate


endmodule


