/*
—È÷§”Ô∑®£∫
1°¢bundle
*/


module id (    
    output wire id_to_exe_bus$id_is_lb,
    output wire id_to_exe_bus$id_is_lbu, 
    output wire id_to_exe_bus$id_is_lh,
    output wire id_to_exe_bus$id_is_lhu,   
    output wire[31:0] id_to_exe_bus$rs_value,  
    output wire[31:0] id_to_exe_bus$rt_value,  
    output wire[4:0] id_to_exe_bus$dest,  
    output wire[31:0] id_to_exe_bus$ds_pc
);
    assign id_to_exe_bus$id_is_lb = 0;
    assign id_to_exe_bus$id_is_lbu = 0;
    assign id_to_exe_bus$id_is_lh = 0;
    assign id_to_exe_bus$id_is_lhu = 1;

    assign id_to_exe_bus$rs_value = 32'ha;
    assign id_to_exe_bus$rt_value = 32'hb;
    assign id_to_exe_bus$dest = 3;
    assign id_to_exe_bus$ds_pc = 32'h80000004;
endmodule

module exe(
    input wire from_id_bus$id_is_lb,
    input wire from_id_bus$id_is_lbu, 
    input wire from_id_bus$id_is_lh,
    input wire from_id_bus$id_is_lhu,   
    input wire[31:0] from_id_bus$rs_value,  
    input wire[31:0] from_id_bus$rt_value,  
    input wire[4:0] from_id_bus$dest,  
    input wire[31:0] from_id_bus$ds_pc,


    output wire id_is_lb,
    output wire id_is_lbu,
    output wire id_is_lh,
    output wire id_is_lhu,
    output wire[31:0] rs_value,
    output wire[31:0] rt_value,
    output wire[4:0] dest,
    output wire[31:0] ds_pc
);
    assign id_is_lb = from_id_bus$id_is_lb;
    assign id_is_lbu = from_id_bus$id_is_lbu;
    assign id_is_lh = from_id_bus$id_is_lh;
    assign id_is_lhu = from_id_bus$id_is_lhu;

    assign rs_value = from_id_bus$rs_value;
    assign rt_value = from_id_bus$rt_value;
    assign dest = from_id_bus$dest;
    assign ds_pc = from_id_bus$ds_pc;
    
endmodule

module top_module(
    output wire bus_out$id_is_lb,
    output wire bus_out$id_is_lbu, 
    output wire bus_out$id_is_lh,
    output wire bus_out$id_is_lhu,   
    output wire[31:0] bus_out$rs_value,  
    output wire[31:0] bus_out$rt_value,  
    output wire[4:0] bus_out$dest,  
    output wire[31:0] bus_out$ds_pc
);
    wire id_to_exe_bus$id_is_lb;
    wire id_to_exe_bus$id_is_lbu;
    wire id_to_exe_bus$id_is_lh;
    wire id_to_exe_bus$id_is_lhu; 
    wire[31:0] id_to_exe_bus$rs_value;
    wire[31:0] id_to_exe_bus$rt_value;
    wire[4:0] id_to_exe_bus$dest;
    wire[31:0] id_to_exe_bus$ds_pc;

    id id_1(
        out.id_to_exe_bus$id_is_lb(id_to_exe_bus$id_is_lb),
        out.id_to_exe_bus$id_is_lbu(id_to_exe_bus$id_is_lbu),
        out.id_to_exe_bus$id_is_lh(id_to_exe_bus$id_is_lh),
        out.id_to_exe_bus$id_is_lhu(id_to_exe_bus$id_is_lhu),   
        out.id_to_exe_bus$rs_value(id_to_exe_bus$rs_value),  
        out.id_to_exe_bus$rt_value(id_to_exe_bus$rt_value),  
        out.id_to_exe_bus$dest(id_to_exe_bus$dest),  
        out.id_to_exe_bus$ds_pc(id_to_exe_bus$ds_pc)
    );

    
    bus_out$id_is_lb := id_to_exe_bus.id_is_lb;
    bus_out$id_is_lbu := id_to_exe_bus.id_is_lbu;
    bus_out$id_is_lh := id_to_exe_bus.id_is_lh;
    bus_out$id_is_lhu := id_to_exe_bus.id_is_lhu;

    bus_out$rs_value := id_to_exe_bus.rs_value;
    bus_out$rt_value := id_to_exe_bus.rt_value;
    bus_out$dest := id_to_exe_bus.dest;
    bus_out$ds_pc := id_to_exe_bus.ds_pc;



endmodule