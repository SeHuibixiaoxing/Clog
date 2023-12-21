module alu
#(
  parameter DATA_WIDTH=32,
  parameter OP_NUM=10
)
(
  input  wire [OP_NUM - 1:0] alu_op,
  input  wire [DATA_WIDTH - 1:0] alu_src1,
  input  wire [DATA_WIDTH - 1:0] alu_src2,
  output wire [DATA_WIDTH - 1:0] alu_result
);


// operation decode
wire op_add;  
wire op_sub;   
wire op_slt;   
wire op_sltu;  
wire op_and;   
wire op_nor;   
wire op_or;    
wire op_xor;   
wire op_sll;   
wire op_srl;   
wire op_sra;   
wire op_lui;   

assign op_add  = alu_op[ 0];
assign op_sub  = alu_op[ 1];
assign op_slt  = alu_op[ 2];
assign op_sltu = alu_op[ 3];
assign op_and  = alu_op[ 4];
assign op_nor  = alu_op[ 5];
assign op_or   = alu_op[ 6];
assign op_xor  = alu_op[ 7];
assign op_sll  = alu_op[ 8];
assign op_srl  = alu_op[ 9];
assign op_sra  = alu_op[10];
assign op_lui  = alu_op[11];

// 32-bit adder
wire [DATA_WIDTH - 1: 0] adder_a;
wire [DATA_WIDTH - 1: 0] adder_b;
wire        adder_cin;
wire [DATA_WIDTH - 1: 0] adder_result;
wire        adder_cout;
assign adder_a   = alu_src1;
assign adder_b   = (op_sub | op_slt | op_sltu) ? ~alu_src2 : alu_src2;
assign adder_cin = (op_sub | op_slt | op_sltu) ? 1'b1      : 1'b0;
assign {adder_cout, adder_result} = adder_a + adder_b + adder_cin;

// ADD, SUB
wire [DATA_WIDTH - 1: 0] add_sub_result; 
assign add_sub_result = adder_result;

// SLT
wire [DATA_WIDTH - 1: 0] slt_result; 
assign slt_result[31:1] = 0;
assign slt_result[0]    = (alu_src1[DATA_WIDTH - 1] & ~alu_src2[DATA_WIDTH - 1])
                        | ((alu_src1[DATA_WIDTH - 1] ~^ alu_src2[DATA_WIDTH - 1]) & adder_result[DATA_WIDTH - 1]);

// SLTU
wire [DATA_WIDTH - 1: 0] sltu_result;
assign sltu_result[DATA_WIDTH - 1:1] = 0;
assign sltu_result[0]    = ~adder_cout;

// bit operation
wire [DATA_WIDTH - 1: 0] and_result;
wire [DATA_WIDTH - 1: 0] nor_result;
wire [DATA_WIDTH - 1: 0] or_result;
wire [DATA_WIDTH - 1: 0] xor_result;
assign and_result = alu_src1 & alu_src2;
assign or_result  = alu_src1 | alu_src2;
assign nor_result = ~or_result;
assign xor_result = alu_src1 ^ alu_src2;

// LUI
wire [DATA_WIDTH - 1: 0] lui_result;
assign lui_result = {alu_src2[DATA_WIDTH / 2 - 1:0], {(DATA_WIDTH/2){1'b0}}};

// SLL  
wire [DATA_WIDTH - 1: 0] sll_result; 
assign sll_result = alu_src2 << alu_src1[4:0];

// SRL, SRA
wire [DATA_WIDTH*2 - 1: 0] sr64_result; 
assign sr64_result = {{DATA_WIDTH{op_sra & alu_src2[DATA_WIDTH - 1]}}, alu_src2[DATA_WIDTH - 1:0]} >> alu_src1[4:0];

// alu result generate
assign alu_result = ({DATA_WIDTH{op_add|op_sub}} & add_sub_result)
                  | ({DATA_WIDTH{op_slt       }} & slt_result)
                  | ({DATA_WIDTH{op_sltu      }} & sltu_result)
                  | ({DATA_WIDTH{op_and       }} & and_result)
                  | ({DATA_WIDTH{op_nor       }} & nor_result)
                  | ({DATA_WIDTH{op_or        }} & or_result)
                  | ({DATA_WIDTH{op_xor       }} & xor_result)
                  | ({DATA_WIDTH{op_lui       }} & lui_result)
                  | ({DATA_WIDTH{op_sll       }} & sll_result)
                  | ({DATA_WIDTH{op_srl|op_sra}} & sr64_result[DATA_WIDTH - 1:0]);

endmodule
