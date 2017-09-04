static void drawLine(byte[] screen, int width, int x1, int x2, int y) {
    int start_offset = x1 % 8;
    int first_full_byte = x1 / 8;
    if (start_offset != 0) first_full_byte++;

    int end_offset = x2 % 8;
    int last_full_byte = x2 / 8;
    if (last_full_byte != 7) last_full_byte--;

    //set full bytes
    for (int b = first_full_byte; b <= last_full_byte; b++) {
        screen[(width / 8) * y + b] = (byte) 0xFF; 
    } 

    //create masks for start and end
    byte start_mask = (byte) (0xFF >> start_offset);
    byte end_mask = (byte) ~(0xFF >> (end_offset + 1));

    //set start and end of line
    if ((x1 / 8) == (x2 / 8)) { //x1 and x2 are on the same line
        byte mask = (byte) (start_mask & end_mask);
        screen[(width / 8) * y + (x1 / 8)] |= mask;
    } else {
        if (start_offset != 0) {
            int byte_pos = (width / 8) * y + first_full_byte - 1;
            screen[byte_pos] |= start_mask;
        }
        if (end_offset != 7) {
            int byte_pos = (width / 8) * y + last_full_byte + 1;
            screen[byte_pos] |= end_mask;
        }
    }
}