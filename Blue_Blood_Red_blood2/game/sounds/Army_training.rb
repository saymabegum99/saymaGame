use_bpm 98

a = [0,0,1,0,1,0,3,0,2,0,0,1,0,0,1,0]

live_loop :drum1 do
  16.times do |i|
    puts a[i], i
    sample :bd_haus if a[i] == 1
    sample :sn_zome if a[i] == 2
    sample :elec_soft_kick if a[i] == 3
    sleep 0.25
    
  end
  
  b = [2,2,1,0,0,0,1,0,2,0,2,0,2,3,2,0]
  
  
  live_loop :drum2 do
    16.times do |i|
      puts a[i], i
      sample :drum_cymbal_pedal if b[i] == 1
      sample :drum_cymbal_closed if b[i] == 2
      sleep 0.25
      
    end
  end
  
  
  
end


