module regfile(               
    input         clk,

    // read port 1
    input  [5-1:0] raddr1,
    output [32-1:0] rdata1,

    // read port 2
    input  [5-1:0] raddr2,
    output [32-1:0] rdata2,

    // write port
    input         we    ,     
    input  [5-1:0] waddr ,
    input  [32-1:0] wdata
);

reg [32-1:0] rf[32-1:0];

//write
always @(posedge clk) begin
    if (we)
        rf[waddr] <= wdata;
end

//read port 1
assign rdata1 = (raddr1==5'b0) ? 32'b0 : rf[raddr1];

//read port 2
assign rdata2 = (raddr2==5'b0) ? 32'b0 : rf[raddr2];

endmodule