use_synth :dark_ambience
with_fx :reverb, mix: 0.4 do
  
  live_loop :phase1 do
    play choose([:D2,:A4]), attack: 9, release: 6
    sleep 8
  end
  
  live_loop :phase2 do
    play choose([:F3,:G5]), attack: 5, release: 7
    sleep 10
  end
  
  live_loop :phase3 do
    play choose([:C4, :A6]), attack: 8, release: 6
    sleep 11
    play_pattern chord(:E3, :m7)
    sleep 2
  end
  
  live_loop :phase4 do
    sleep 10
    play_pattern_timed scale(:C3, :major), 0.125, release: 1
    
  end
  
end
