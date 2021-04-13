in_thread do
  use_synth :fm
  sleep 2
  loop do
    25.times do
      sample :drum_bass_hard, amp: 1.5
      sleep 0.25
      play :d2, release: 0.8
      sample :elec_hollow_kick, rate: 18, amp: 1.3
      sleep 0.25
    end
    sleep 6
  end
end

use_synth :fm
with_fx :echo do |rev|
  loop do
    
    control rev, mix: rrand(1, 0.3)
    with_fx :echo, phase: 1.5 do
      sample :ambi_piano, sustain: 1, release: 6, amp: 3
    end
    
    control rev, mix: rrand(0.2, 0.6)
    r = rrand(0.5, 0.6)
    64.times do
      play chord(:f4, :major7).choose, release: r, cutoff: rrand(50, 90), amp: 0.5
      sleep 0.125
    end
    
    control rev, mix: rrand(0, 0.6)
    r = rrand(0.1, 0.2)
    with_synth :mod_sine do
      32.times do
        sleep 0.125
        play chord(:d3, :minor).choose, release: r, cutoff: rrand(40, 130), amp: 0.7
      end
    end
    
    control rev, mix: rrand(0, 0.6)
    r = rrand(0.05, 0.3)
    32.times do
      play chord(:e3, :minor).choose, release: r, cutoff: rrand(110, 130), amp: 0.4
      sleep 0.125
    end
    
    control rev, mix: rrand(0, 0.6)
    with_fx :echo, phase: 0.25, decay: 8 do
      16.times do
        play chord([:e2, :e3, :e4].choose, :m7).choose, release: 0.05, cutoff: rrand(50, 129), amp: 0.5
        sleep 0.125
      end
    end
  end
end