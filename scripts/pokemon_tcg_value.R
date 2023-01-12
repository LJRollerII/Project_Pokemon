#Import Packages

library(tidyverse)
library(rvest)

# Web Scrape Data

html <- read_html('https://shop.tcgplayer.com/price-guide/pokemon/base-set') %>%
  html_table(fill = TRUE)

html <- tbl_df(html[[1]] %>% select('PRODUCT', 'Rarity','Number', 'Market Price'))

#Remove the $ in the Market Price column
html$`Market Price` <- gsub('\\$', '', html$`Market Price`)
html$`Market Price` <- as.numeric(html$`Market Price`)

html %>%
  arrange(Number)

my_cards <- read.csv('../data/ptcg_inventory.csv')

cards <- my_cards %>%
  left_join(html, by = c('card' = 'Number')) %>%
  arrange(card)

# Calculate the value of the card collection

cards %>%
  mutate(total_card_value = `Market Price` * count) %>%
  summarize(our_collection_value = sum(total_card_value, na.rm = TRUE))

# What's cards are we missing from the collection?

html %>%
  anti_join(cards, by = c('Number' = 'card')) %>%
  summarize(count = n(),
            money_needed_to_complete_set = sum(`Market Price`))

# Visualizations

html %>%
  filter(`Market Price` < 100)  %>%
  ggplot(aes(x = `Market Price`)) +
  geom_histogram(bins = 10)

