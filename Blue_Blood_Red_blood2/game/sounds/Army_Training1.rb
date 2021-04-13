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
  
  
  with_synth :tech_saws do
    with_fx(:slicer, pulse_width: [0.25,0.125].choose) do
      with_fx(:reverb, damp: 0.5, pre_mix: 0.3) do
        start_note = chord([:D2, :D2, :C1, :C2, :B3, :B3].choose, :major).choose
        final_note = chord([:D1, :D2, :E1, :E2, :F3, :F3].choose, :major).choose
        
        p = play start_note, release: 6, note_slide: 3, cutoff: 25, cutoff_slide: 3,
          detune: rrand(0, 0.2), pan: rrand(-1, 0), pan_slide: rrand(4, 8)
        control p, note: final_note, cutoff: rrand(75, 130), pan: rrand(0, 1)
      end
      
      
    end
  end
  
  sleep 1
end
