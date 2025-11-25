"""use_bpm 104

###############################################
#  DARK DANCEHALL / HIP-HOP RIDDIM
###############################################

# --- Global FX ---
with_fx :reverb, room: 0.6, mix: 0.5 do

  ###############################################
  # DRUMS
  ###############################################
  live_loop :drums do
    sample :bd_haus, amp: 1.6
    sleep 0.5
    sample :bd_haus, amp: 1.4
    sleep 0.25
    sample :sn_zome, amp: 0.8
    sleep 0.25
    sample :bd_haus, amp: 1.3
    sleep 0.5
    sample :sn_zome, amp: 0.9
    sleep 0.5
  end

  ###############################################
  # DARK BASSLINE
  ###############################################
  live_loop :bass, sync: :drums do
    use_synth :fm
    use_synth_defaults amp: 1, depth: 2, divisor: 1

    notes = [:f2, :f2, :ds2, :c2]
    durs  = [0.5, 0.5, 0.5, 0.5]

    notes.zip(durs).each do |n, d|
      play n, release: 0.3
      sleep d
    end
  end

  ###############################################
  # DARK PADS & CHORDS
  ###############################################
  live_loop :pads, sync: :drums do
    use_synth :hollow
    chords = [
      chord(:f3, :minor7),
      chord(:ds3, :minor7),
      chord(:c3, :minor7)
    ]

    chords.each do |ch|
      play ch, sustain: 4, release: 2, amp: 0.6
      sleep 4
    end
  end

  ###############################################
  # LEAD MELODY (Dark Pluck)
  ###############################################
  live_loop :lead, sync: :drums do
    use_synth :pluck
    use_random_seed 1234

    8.times do
      play (scale :f4, :minor_pentatonic).choose,
           release: 0.2,
           amp: 0.9
      sleep 0.5
    end
  end

end"""

    """use_bpm 94  # good fusion tempo

# --- DRUMS ---
live_loop :kick do
  sample :bd_haus, amp: 2
  sleep 0.75
  sample :bd_haus, amp: 1.8
  sleep 0.75
  sleep 0.5
end

live_loop :snare do
  sleep 1
  sample :sn_dolf, amp: 1.5
  sleep 1
end

live_loop :hats do
  sleep 0.25
  sample :hat_808, amp: 0.7, rate: 1.2
  sleep 0.25
end

# --- DANCEHALL DEMBOW ---
live_loop :dembow do
  sync :kick
  sample :perc_snap, amp: 1.5
  sleep 0.5
  sample :perc_snap, amp: 1
  sleep 0.25
  sleep 0.25
  sample :perc_snap, amp: 1.3
  sleep 0.5
end

# --- BASS ---
live_loop :bass do
  use_synth :fm
  use_synth_defaults depth: 2, divisor: 1, amp: 1.4
  notes = [:c2, :c2, :eb2, :g2]
  play notes.tick, release: 0.3
  sleep 0.75
end

# --- MELODY / PLUCK ---
live_loop :melody do
  use_synth :pluck
  play_pattern_timed [:c4, :g4, :bb4, :g4], [0.5, 0.5, 0.25, 0.75], amp: 1
  sleep 1
end
    """
    """use_bpm 104

# --- Dark Pad / Atmosphere ---
live_loop :dark_pad do
  use_synth :hollow
  play_chord (chord :e2, :minor7), attack: 2, sustain: 6, release: 4, amp: 0.6
  sleep 8
end

# --- Chord Stabs ---
live_loop :chords, sync: :dark_pad do
  use_synth :prophet
  with_fx :reverb, mix: 0.4 do
    play (chord :e3, :minor7).choose, attack: 0.1, sustain: 0.3, release: 0.4, amp: 0.9
  end
  sleep 2
end

# --- Bass Line (Dark, heavy, simple) ---
live_loop :bass, sync: :dark_pad do
  use_synth :fm
  notes = [:e2, :g2, :a2, :g2]
  times = [1, 1, 1, 1]
  
  notes.zip(times).each do |n, t|
    play n, release: 0.6, amp: 1.4, cutoff: 80
    sleep t
  end
end

# --- Minimal Dancehall Drums (Fewer hits) ---
live_loop :drums, sync: :dark_pad do
  # light kick every bar
  sample :bd_haus, amp: 1.2
  sleep 1
  
  # ghost snare (soft)
  sample :sn_zome, amp: 0.4
  sleep 1
  
  # kick again
  sample :bd_haus, amp: 1.2
  sleep 1
  
  # rimshot instead of heavy snare
  sample :elec_tick, amp: 0.7
  sleep 1
end
    """
    
    """use_bpm 140

### DARK CHORD PAD ###
live_loop :pad, sync: :kick do
  use_synth :hollow
  play_chord [:g3, :bb3, :d4], sustain: 4, release: 2, amp: 0.6
  sleep 4
end

### GUITAR-LIKE PLUCK (ROCKSTAR FEEL) ###
live_loop :pluck, sync: :kick do
  use_synth :pluck
  with_fx :reverb, mix: 0.5, room: 0.8 do
    notes = [:d5, :bb4, :g4, :d5]
    notes.each do |n|
      play n, amp: 0.8, release: 0.3, cutoff: 90
      sleep 0.5
    end
  end
end

### 808 BASS (MINIMAL & CLEAN) ###
live_loop :bass, sync: :kick do
  use_synth :fm
  use_synth_defaults release: 0.4, amp: 1.2, depth: 2
  play :g2
  sleep 1
  play :g2
  sleep 1
  play :bb2
  sleep 2
end

### SPARSE KICK ###
live_loop :kick do
  sample :bd_haus, amp: 1
  sleep 1
  sleep 0.5
  sample :bd_haus, amp: 0.8
  sleep 2.5
end

### LIGHT SNARE (ROCKSTAR STYLE) ###
live_loop :snare, sync: :kick do
  sleep 1
  sample :sn_generic, amp: 1.5
  sleep 2
end

### HIHATS WITH SWING ###
live_loop :hats, sync: :kick do
  with_fx :lpf, cutoff: 100 do
    sleep 0.25
    7.times do
      sample :drum_cymbal_closed, amp: 0.6
      sleep (ring 0.25, 0.23, 0.27, 0.25).tick # small swing
    end
  end
end

### VOCAL AD-LIB STYLE FX ###
live_loop :adlibs, sync: :kick do
  with_fx :echo, phase: 0.375, mix: 0.25 do
    sample :perc_snap, amp: 0.7 if one_in(8)
    sample :elec_blip2, amp: 0.3, rate: -1 if one_in(12)
  end
  sleep 2
end

    """