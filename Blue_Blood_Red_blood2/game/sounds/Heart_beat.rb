with_fx :echo do
  in_thread do
    loop do
      r = [0.2, 0.4, 0.4].choose
      10.times do
        sample :ambi_piano, rate: r, pan: rrand(-0.5, 1)
        sleep 0.5
      end
    end
  end
end

with_fx :slicer do
  in_thread do
    loop do
      sleep 5
      r = [0.2, 0.4, 0.4].choose
      10.times do
        sample :ambi_swoosh, rate: r, pan: rrand(-0.4, 0.8)
        sleep 0.8
      end
    end
  end
end



