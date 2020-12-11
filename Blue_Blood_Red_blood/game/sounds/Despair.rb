use_synth :hollow
with_fx :reverb, room: 0.4 do
  
  live_loop :phase1 do
    play choose([:D4,:C4]), attack: 9, release: 6
    sleep 8
  end
  
  live_loop :phase2 do
    play choose([:A4,:C4]), attack: 5, release: 7
    sleep 10
  end
  
  live_loop :phase3 do
    play choose([:D4, :A4]), attack: 8, release: 6
    sleep 11
    play_pattern chord(:A4, :major7)
    sleep 2
  end
  
  live_loop :phase4 do
    sleep 10
    play_pattern_timed chord(:C4, :major), [2, 1]
    
    
  end
  
end
