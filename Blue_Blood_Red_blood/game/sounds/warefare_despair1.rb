use_synth :hollow
with_fx :reverb, room: 0.4 do
  
  live_loop :phase1 do
    play choose([:A3,:E3]), attack: 9, release: 6
    sleep 8
  end
  
  live_loop :phase2 do
    play choose([:B3,:D3]), attack: 5, release: 7
    sleep 10
  end
  
  live_loop :phase3 do
    play choose([:E3, :C3]), attack: 8, release: 6
    sleep 11
    
  end
  
  live_loop :phase4 do
    play_pattern_timed chord(:C2, :major), [0.25, 0.5]
    
  end
  
  live_loop :phase5 do
    use_synth :dark_ambience
    with_fx :reverb, room: 0.4 do
      sleep 11
      sample :ambi_haunted_hum, rate: rrand(-1.5, 0.5)
      
    end
    
  end
end
