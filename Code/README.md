# Code-Challenge

For this task, I will determine the relationships between database tables as described across a series of configuration files in JSON.

## My Answer

The full dependencies relationships set then looks like this in ascii:

```bash
games.nulls
   |
   |+crosscheck.tags
             |
             |+base.games
             |
             |+scout.tags
                       |
                       |+base.tags
                       |
                       |+dict.player_dedup
```


Any other notes that you think valuable for us to know