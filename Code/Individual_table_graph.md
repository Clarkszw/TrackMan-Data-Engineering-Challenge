# Individual table graph from table JSON files

```bash
crosscheck.calibration_maintenance
   |
   |+base.calibration_maintenance
   |
   |+crosscheck.calibrations
   |
   |+crosscheck.games

crosscheck.games
    |
    |+base.games
    |
    |+base.locations
    |
    |+rundown.location_history
    |
    |+crosscheck.tags
         |
         |+scout.tags
         |
         |+base.games

crosscheck.tags
    |
    |+scout.tags
    |
    |+base.games

games.autorecalibration
   |
   |+crosscheck.calibrations
   |
   |+crosscheck.games
   |
   |+crosscheck.calibration_maintenance

games.latency
   |
   |+advance.merged_measurement
   |
   |+sdkjson.live_pitch_data
   |
   |+sdkjson.measurement
   |
   |+crosscheck.tags

games.live_final
   |
   |+merged.measurement
   |
   |+merged.live_pitch_data
   |
   |+merged.batting_launch_data
   |
   |+crosscheck.tags

games.metadata
   |
   |+base.games
   |
   |+base.locations
   |
   |+rundown.location_history

games.nulls
   |
   |+crosscheck.tags

games.oem
   |
   |+radar.measurement
   |
   |+radar.live_pitch_data
   |
   |+crosscheck.tags

games.vision_oem
   |
   |+radar.measurement
   |
   |+radar.live_pitch_data
   |
   |+merged.measurement
   |
   |+vision.live_pitch_data
   |
   |+crosscheck.tags

games.vision
   |
   |+vision.final_pitch_data
   |
   |+merged.measurement
   |
   |+vision.live_pitch_data
   |
   |+crosscheck.tags

locations.latency
   |
   |+merged.measurement
   |
   |+sdkjson.live_pitch_data
   |
   |+sdkjson.measurement
   |
   |+crosscheck.tags
   |
   |+base.games

locations.vision_oem
   |
   |+radar.measurement
   |
   |+radar.live_pitch_data
   |
   |+merged.measurement
   |
   |+vision.live_pitch_data
   |
   |+base.locations
   |
   |+crosscheck.tags

report.delivered_combined_hist
   |
   |+report.delivered_no_exceptions_hist
   |
   |+report.delivered_exceptions_hist

report.delivered_exceptions_hist
   |
   |+report.delivered_new_pk
   |
   |+base.games
   |
   |+report.exp_access_rules_hist

report.delivered_new_pk
   |
   |+broadcast.delivered_games

report.delivered_no_exceptions_hist
   |
   |+report.delivered_new_pk
   |
   |+base.games
   |
   |+report.exp_access_rules_hist

report.delivered_no_exceptions
   |
   |+report.delivered_new_pk
   |
   |+base.games
   |
   |+report.exp_access_rules

report.exp_access_rules_hist
   |
   |+rundown.access_rules_end
   |
   |+broadcast.priority_lists

report.exp_access_rules
   |
   |+broadcast.access_rules
   |
   |+broadcast.priority_lists

report.false_delivered_hist
   |
   |+report.delivered_new_pk
   |
   |+report.delivered_combined_hist

report.hardball_pitchers
   |
   |+scout.tags
   |
   |+base.measurements
   |
   |+base.games

report.mlb_orgs
   |
   |+dict.team_org
   |
   |+scout.teams

report.practice_pitching_dev
   |
   |+practice.plays_dev
   |
   |+practice.games_dev

report.practice_pitching
   |
   |+practice.plays
   |
   |+practice.games

report.schedule_new_level
   |
   |+lineup.schedule

report.scheduled_combined
   |
   |+report.scheduled_no_exceptions
   |
   |+report.scheduled_exceptions

report.scheduled_exceptions
   |
   |+lineup.schedule
   |
   |+games.metadata
   |
   |+report.exp_access_rules

report.scheduled_no_exceptions_hist
   |
   |+report.schedule_new_level
   |
   |+games.metadata
   |
   |+report.exp_access_rules_hist

report.scheduled_no_exceptions
   |
   |+lineup.schedule
   |
   |+games.metadata
   |
   |+report.exp_access_rules

report.verified_levels_18
   |
   |+base.locations
   |
   |+base.games
   |
   |+dict.game_type

rundown.access_rules_history
   |
   |+rundown.access_rules_rows
   |
   |+rundown.access_rules_rows
   |
   |+broadcast.access_rules

rundown.access_rules_rows
   |
   |+rundown.access_rules
   |
   |+broadcast.access_rules

rundown.location_history_rows
   |
   |+rundown.locations

rundown.location_history
   |
   |+rundown.location_history_rows
   |
   |+rundown.location_history_rows

scout.tags
   |
   |+base.tags
   |
   |+dict.player_dedup

trout.app_angle
   |
   |+scout.tags
   |
   |+base.measurements
   |
   |+base.games
   |
   |+base.players
   |
   |+report.hardball_ref

```