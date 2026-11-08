# Events

Checked with RegisterEvent. Payloads are Blizzard's; "seen" counts and argument kinds are what fired while the probe was on (n number, s string, b boolean, t table, S secret, - nil).

| | Event | Seen | Argument kinds seen | Page |
|---|---|---|---|---|
| ✅ | `ACCOUNT_CHARACTER_CURRENCY_DATA_RECEIVED` |  |  | [CurrencySystem](systems/CurrencySystem.md) |
| 🆕 | `ACCOUNT_CHARACTER_LIST_RECIEVED` |  |  | used in `Blizzard_GlueXML/Camelot/CharacterCopy.lua` |
| 🆕 | `ACCOUNT_CONVERSION_DISPLAY_STATE` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectUI.lua` |
| ✅ | `ACCOUNT_CVARS_LOADED` |  |  | [Glue](systems/Glue.md) |
| 🆕 | `ACCOUNT_DATA_INITIALIZED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `ACCOUNT_DATA_RESTORED` |  |  | used in `Blizzard_GlueXML/Camelot/CharacterCopy.lua` |
| 🆕 | `ACCOUNT_DATA_RESTORING` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `ACCOUNT_LOCKED_POST_SAVE_UPDATE` |  |  | used in `Blizzard_AccountSaveUI/Blizzard_AccountSaveUI.lua` |
| ✅ | `ACCOUNT_MONEY` |  |  | [CurrencySystem](systems/CurrencySystem.md) |
| 🆕 | `ACCOUNT_SAVE_ENABLED_UPDATE` |  |  | used in `Blizzard_AccountSaveUI/Blizzard_AccountSaveUI.lua` |
| 🆕 | `ACCOUNT_SAVE_RESULT` |  |  | used in `Blizzard_AccountSaveUI/Blizzard_AccountSaveUI.lua` |
| ✅ | `ACCOUNT_STORE_CURRENCY_AVAILABLE_UPDATED` |  |  | [AccountStore](systems/AccountStore.md) |
| ✅ | `ACCOUNT_STORE_FRONT_UPDATED` |  |  | [AccountStore](systems/AccountStore.md) |
| ✅ | `ACCOUNT_STORE_ITEM_INFO_UPDATED` |  |  | [AccountStore](systems/AccountStore.md) |
| ✅ | `ACCOUNT_STORE_TRANSACTION_ERROR` |  |  | [AccountStore](systems/AccountStore.md) |
| ⛔ | `ACHIEVEMENT` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `ACHIEVEMENT_EARNED` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `ACHIEVEMENT_PLAYER_NAME` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `ACHIEVEMENT_SEARCH_UPDATED` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `ACTIONBAR_HIDEGRID` |  |  | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTIONBAR_PAGE_CHANGED` |  |  | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTIONBAR_SHOWGRID` |  |  | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTIONBAR_SHOW_BOTTOMLEFT` |  |  | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTIONBAR_SLOT_CHANGED` |  |  | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTIONBAR_UPDATE_COOLDOWN` | 31 | `` | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTIONBAR_UPDATE_STATE` | 44 | `` | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTIONBAR_UPDATE_USABLE` | 16 | `` | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTION_RANGE_CHECK_UPDATE` | 124 | `n,b,b` | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTION_USABLE_CHANGED` | 16 | `t` | [ActionBar](systems/ActionBar.md) |
| ✅ | `ACTION_WILL_BIND_ITEM` |  |  | [Item](systems/Item.md) |
| ✅ | `ACTIVATE_GLYPH` |  |  | [GlyphInfo](systems/GlyphInfo.md) |
| ✅ | `ACTIVE_COMBAT_CONFIG_CHANGED` |  |  | [ClassTalents](systems/ClassTalents.md) |
| ✅ | `ACTIVE_DELVE_DATA_UPDATE` |  |  | [DelvesUI](systems/DelvesUI.md) |
| ✅ | `ACTIVE_GAME_MODE_UPDATED` |  |  | [GameRules](systems/GameRules.md) |
| 🆕 | `ACTIVE_MAP_SCENE_TRANSITIONED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `ACTIVE_PLAYER_SPECIALIZATION_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `ACTIVE_TALENT_GROUP_CHANGED` |  |  | [SpecializationInfo](systems/SpecializationInfo.md) |
| ✅ | `ADAPTER_LIST_CHANGED` |  |  | [Video](systems/Video.md) |
| ✅ | `ADDONS_UNLOADING` | 1 | `b` | [AddOns](systems/AddOns.md) |
| ✅ | `ADDON_ACTION_BLOCKED` |  |  | [RestrictedActions](systems/RestrictedActions.md) |
| ✅ | `ADDON_ACTION_FORBIDDEN` | 8 | `s,s` | [RestrictedActions](systems/RestrictedActions.md) |
| ✅ | `ADDON_LOADED` | 33 | `s,b` | [AddOns](systems/AddOns.md) |
| ✅ | `ADDON_RESTRICTION_STATE_CHANGED` | 2 | `n,n` | [RestrictedActions](systems/RestrictedActions.md) |
| ⛔ | `ADD_GUILDMEMBER` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ⛔ | `ADD_GUILDMEMBER_WITH_FINDER_LINK` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ✅ | `ADD_NEIGHBORHOOD_CHARTER_SIGNATURE` |  |  | [HousingUI](systems/HousingUI.md) |
| ⛔ | `ADVANCED_COOLDOWN_SETTINGS` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ⛔ | `ADVANCED_COOLDOWN_SETTINGS1` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ⛔ | `ADVENTURER` |  |  | used in `Blizzard_SharedXML/ClassColors.lua` |
| ✅ | `ADVENTURE_MAP_CLOSE` |  |  | [AdventureMap](systems/AdventureMap.md) |
| ✅ | `ADVENTURE_MAP_OPEN` |  |  | [AdventureMap](systems/AdventureMap.md) |
| ✅ | `ADVENTURE_MAP_QUEST_UPDATE` |  |  | [AdventureMap](systems/AdventureMap.md) |
| ✅ | `ADVENTURE_MAP_UPDATE_INSETS` |  |  | [AdventureMap](systems/AdventureMap.md) |
| ✅ | `ADVENTURE_MAP_UPDATE_POIS` |  |  | [AdventureMap](systems/AdventureMap.md) |
| ✅ | `AJ_DUNGEON_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_OPEN` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_OPEN_COLLECTIONS_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_PVE_LFG_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_PVP_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_PVP_LFG_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_PVP_RBG_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_PVP_SKIRMISH_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_PVP_SPECIAL_BG_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_PVP_TRAINING_GROUNDS_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_QUEST_LOG_OPEN` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_RAID_ACTION` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_REFRESH_DISPLAY` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `AJ_REWARD_DATA_RECEIVED` |  |  | [AdventureJournal](systems/AdventureJournal.md) |
| ✅ | `ALERT_AGE_VERIFICATION_RESTRICTED` |  |  | [SocialRestrictions](systems/SocialRestrictions.md) |
| ✅ | `ALERT_REGIONAL_CHAT_DISABLED` |  |  | [SocialRestrictions](systems/SocialRestrictions.md) |
| ✅ | `ALLIED_RACE_CLOSE` |  |  | [AlliedRaces](systems/AlliedRaces.md) |
| ✅ | `ALLIED_RACE_OPEN` |  |  | [AlliedRaces](systems/AlliedRaces.md) |
| 🆕 | `ALL_WARBAND_GROUP_SCENES_UPDATED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `ALTERNATIVE_DEFAULT_LANGUAGE_CHANGED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `ANIMA_DIVERSION_CLOSE` |  |  | [AnimaDiversionInfo](systems/AnimaDiversionInfo.md) |
| ✅ | `ANIMA_DIVERSION_OPEN` |  |  | [AnimaDiversionInfo](systems/AnimaDiversionInfo.md) |
| ✅ | `ANIMA_DIVERSION_TALENT_UPDATED` |  |  | [AnimaDiversionInfo](systems/AnimaDiversionInfo.md) |
| ⛔ | `APPLAUD` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `ARCHAEOLOGY_CLOSED` |  |  | [ResearchInfo](systems/ResearchInfo.md) |
| ✅ | `ARCHAEOLOGY_FIND_COMPLETE` |  |  | [ResearchInfo](systems/ResearchInfo.md) |
| ✅ | `ARCHAEOLOGY_SURVEY_CAST` |  |  | [ResearchInfo](systems/ResearchInfo.md) |
| ✅ | `ARCHAEOLOGY_TOGGLE` |  |  | [ResearchInfo](systems/ResearchInfo.md) |
| ⛔ | `AREA_NOT_EXPLORED` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ✅ | `AREA_POIS_UPDATED` |  |  | [AreaPoiInfo](systems/AreaPoiInfo.md) |
| ✅ | `AREA_SPIRIT_HEALER_IN_RANGE` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `AREA_SPIRIT_HEALER_OUT_OF_RANGE` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `ARENA_COOLDOWNS_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `ARENA_CROWD_CONTROL_SPELL_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `ARENA_OPPONENT_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `ARENA_PREP_OPPONENT_SPECIALIZATIONS` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `ARENA_SEASON_WORLD_STATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ⛔ | `ARENA_TEAM_ROSTER_UPDATE` |  |  | used in `Blizzard_UIPanels_Game/Cata/PVPFrame.lua` |
| ⛔ | `ARENA_TEAM_UPDATE` |  |  | used in `Blizzard_UIPanels_Game/Cata/PVPFrame.lua` |
| ✅ | `ARTIFACT_CLOSE` | 1 | `` | [ArtifactUI](systems/ArtifactUI.md) |
| ✅ | `ARTIFACT_DIGSITE_COMPLETE` |  |  | [ResearchInfo](systems/ResearchInfo.md) |
| ✅ | `ARTIFACT_ENDGAME_REFUND` |  |  | [ArtifactUI](systems/ArtifactUI.md) |
| ✅ | `ARTIFACT_RELIC_FORGE_CLOSE` |  |  | [ArtifactUI](systems/ArtifactUI.md) |
| ✅ | `ARTIFACT_RELIC_FORGE_PREVIEW_RELIC_CHANGED` |  |  | [ArtifactUI](systems/ArtifactUI.md) |
| ✅ | `ARTIFACT_RELIC_FORGE_UPDATE` |  |  | [ArtifactUI](systems/ArtifactUI.md) |
| ✅ | `ARTIFACT_RELIC_INFO_RECEIVED` |  |  | [ArtifactUI](systems/ArtifactUI.md) |
| ✅ | `ARTIFACT_RESPEC_PROMPT` |  |  | [ArtifactUI](systems/ArtifactUI.md) |
| ✅ | `ARTIFACT_TIER_CHANGED` |  |  | [ArtifactUI](systems/ArtifactUI.md) |
| ✅ | `ARTIFACT_UPDATE` |  |  | [ArtifactUI](systems/ArtifactUI.md) |
| ✅ | `ARTIFACT_XP_UPDATE` |  |  | [ArtifactUI](systems/ArtifactUI.md) |
| 🆕 | `ASSIGN_VAS_RESPONSE` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| ✅ | `ASSISTED_COMBAT_ACTION_SPELL_CAST` |  |  | [AssistedCombat](systems/AssistedCombat.md) |
| ⛔ | `ASSISTED_COMBAT_ROTATION` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ⛔ | `ATTACKMYTARGET` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `AUCTION_CANCELED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_AUCTIONS_EXPIRED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_AUCTION_CREATED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_BROWSE_FAILURE` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_BROWSE_RESULTS_ADDED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_BROWSE_RESULTS_UPDATED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_CLOSED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_DISABLED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_FAVORITES_UPDATED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_ITEM_DELIVERY_DELAY_UPDATE` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_NEW_BID_RECEIVED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_NEW_RESULTS_RECEIVED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_POST_ERROR` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_POST_WARNING` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_PURCHASE_COMPLETED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_SCRIPT_DEPRECATED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_SHOW` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_SHOW_COMMODITY_WON_NOTIFICATION` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_SHOW_ERROR` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_SHOW_FORMATTED_NOTIFICATION` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_SHOW_NOTIFICATION` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_THROTTLED_MESSAGE_DROPPED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_THROTTLED_MESSAGE_QUEUED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_THROTTLED_MESSAGE_RESPONSE_RECEIVED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_THROTTLED_MESSAGE_SENT` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_HOUSE_THROTTLED_SYSTEM_READY` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_MULTISELL_FAILURE` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_MULTISELL_START` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AUCTION_MULTISELL_UPDATE` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `AURA_DATA_PROVIDER_SWITCH` |  |  | [UnitAuras](systems/UnitAuras.md) |
| 🆕 | `AUTH_CHALLENGE_FINISHED` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| ✅ | `AUTOFOLLOW_BEGIN` |  |  | [Unit](systems/Unit.md) |
| ✅ | `AUTOFOLLOW_END` |  |  | [Unit](systems/Unit.md) |
| 🆕 | `AUTO_REALM_SWAP` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `AVAILABLE_GAME_MODES_UPDATED` |  |  | [GameRules](systems/GameRules.md) |
| ✅ | `AVATAR_LIST_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `AVOIDANCE_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `AZERITE_EMPOWERED_ITEM_EQUIPPED_STATUS_CHANGED` |  |  | [AzeriteEmpoweredItem](systems/AzeriteEmpoweredItem.md) |
| ✅ | `AZERITE_EMPOWERED_ITEM_LOOTED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `AZERITE_EMPOWERED_ITEM_SELECTION_UPDATED` |  |  | [AzeriteEmpoweredItem](systems/AzeriteEmpoweredItem.md) |
| ✅ | `AZERITE_ESSENCE_ACTIVATED` |  |  | [AzeriteEssence](systems/AzeriteEssence.md) |
| ✅ | `AZERITE_ESSENCE_ACTIVATION_FAILED` |  |  | [AzeriteEssence](systems/AzeriteEssence.md) |
| ✅ | `AZERITE_ESSENCE_CHANGED` |  |  | [AzeriteEssence](systems/AzeriteEssence.md) |
| ✅ | `AZERITE_ESSENCE_FORGE_CLOSE` |  |  | [AzeriteEssence](systems/AzeriteEssence.md) |
| ✅ | `AZERITE_ESSENCE_FORGE_OPEN` |  |  | [AzeriteEssence](systems/AzeriteEssence.md) |
| ✅ | `AZERITE_ESSENCE_MILESTONE_UNLOCKED` |  |  | [AzeriteEssence](systems/AzeriteEssence.md) |
| ✅ | `AZERITE_ESSENCE_UPDATE` |  |  | [AzeriteEssence](systems/AzeriteEssence.md) |
| ✅ | `AZERITE_ITEM_ENABLED_STATE_CHANGED` |  |  | [AzeriteItem](systems/AzeriteItem.md) |
| ✅ | `AZERITE_ITEM_EXPERIENCE_CHANGED` |  |  | [AzeriteItem](systems/AzeriteItem.md) |
| ✅ | `AZERITE_ITEM_POWER_LEVEL_CHANGED` |  |  | [AzeriteItem](systems/AzeriteItem.md) |
| ✅ | `BAG_CLOSED` |  |  | [Container](systems/Container.md) |
| ✅ | `BAG_CONTAINER_UPDATE` | 1 | `` | [Container](systems/Container.md) |
| ✅ | `BAG_NEW_ITEMS_UPDATED` |  |  | [Container](systems/Container.md) |
| ✅ | `BAG_OPEN` |  |  | [Container](systems/Container.md) |
| ✅ | `BAG_OVERFLOW_WITH_FULL_INVENTORY` |  |  | [Container](systems/Container.md) |
| ✅ | `BAG_SLOT_FLAGS_UPDATED` |  |  | [Container](systems/Container.md) |
| ✅ | `BAG_UPDATE` | 8 | `n` | [Container](systems/Container.md) |
| ✅ | `BAG_UPDATE_COOLDOWN` | 15 | `` | [Container](systems/Container.md) |
| ✅ | `BAG_UPDATE_DELAYED` | 3 | `` | [Container](systems/Container.md) |
| ✅ | `BANKFRAME_CLOSED` |  |  | [Bank](systems/Bank.md) |
| ✅ | `BANKFRAME_OPENED` |  |  | [Bank](systems/Bank.md) |
| ✅ | `BANK_BAG_SLOT_FLAGS_UPDATED` |  |  | [Bank](systems/Bank.md) |
| ✅ | `BANK_TABS_CHANGED` |  |  | [Bank](systems/Bank.md) |
| ✅ | `BANK_TAB_SETTINGS_UPDATED` |  |  | [Bank](systems/Bank.md) |
| ✅ | `BARBER_SHOP_APPEARANCE_APPLIED` |  |  | [BarberShop](systems/BarberShop.md) |
| ✅ | `BARBER_SHOP_CAMERA_VALUES_UPDATED` |  |  | [BarberShop](systems/BarberShop.md) |
| ✅ | `BARBER_SHOP_CLOSE` |  |  | [BarberShop](systems/BarberShop.md) |
| ✅ | `BARBER_SHOP_COST_UPDATE` |  |  | [BarberShop](systems/BarberShop.md) |
| ✅ | `BARBER_SHOP_FORCE_CUSTOMIZATIONS_UPDATE` |  |  | [BarberShop](systems/BarberShop.md) |
| ✅ | `BARBER_SHOP_OPEN` |  |  | [BarberShop](systems/BarberShop.md) |
| ✅ | `BARBER_SHOP_RESULT` |  |  | [BarberShop](systems/BarberShop.md) |
| ✅ | `BATTLEFIELDS_CLOSED` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `BATTLEFIELDS_SHOW` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `BATTLEFIELD_AUTO_QUEUE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `BATTLEFIELD_AUTO_QUEUE_EJECT` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `BATTLEFIELD_QUEUE_TIMEOUT` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `BATTLEGROUND_OBJECTIVES_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `BATTLEGROUND_POINTS_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `BATTLEPET_FORCE_NAME_DECLENSION` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `BATTLE_NET_FRIEND_TAG_ENABLED_STATUS_UPDATED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BATTLE_NET_TITLE_FRIEND_CUSTOM_NAME_ENABLED_STATUS_UPDATED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BATTLE_PET_CURSOR_CLEAR` |  |  | [Cursor](systems/Cursor.md) |
| ✅ | `BC_26_COLD_SWAP_FEATURE_ENABLED_CHANGED` |  |  | [BlizzCon2026Scripts](systems/BlizzCon2026Scripts.md) |
| ✅ | `BC_26_EXPERIENCE_CHANGED` |  |  | [BlizzCon2026Scripts](systems/BlizzCon2026Scripts.md) |
| ✅ | `BEHAVIORAL_NOTIFICATION` |  |  | [BehavioralMessaging](systems/BehavioralMessaging.md) |
| ✅ | `BIDS_UPDATED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `BID_ADDED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ⛔ | `BID_AUCTION` |  |  | used in `Blizzard_AuctionHouseUI/Shared/Blizzard_AuctionHouseFrame.lua` |
| ✅ | `BINDINGS_LOADED` | 1 | `` | [KeyBindings](systems/KeyBindings.md) |
| ✅ | `BIND_ENCHANT` |  |  | [Item](systems/Item.md) |
| ✅ | `BLACK_MARKET_BID_RESULT` |  |  | [BlackMarketInfo](systems/BlackMarketInfo.md) |
| ✅ | `BLACK_MARKET_CLOSE` |  |  | [BlackMarketInfo](systems/BlackMarketInfo.md) |
| ✅ | `BLACK_MARKET_ITEM_UPDATE` |  |  | [BlackMarketInfo](systems/BlackMarketInfo.md) |
| ✅ | `BLACK_MARKET_OPEN` |  |  | [BlackMarketInfo](systems/BlackMarketInfo.md) |
| ✅ | `BLACK_MARKET_OUTBID` |  |  | [BlackMarketInfo](systems/BlackMarketInfo.md) |
| ✅ | `BLACK_MARKET_UNAVAILABLE` |  |  | [BlackMarketInfo](systems/BlackMarketInfo.md) |
| ✅ | `BLACK_MARKET_WON` |  |  | [BlackMarketInfo](systems/BlackMarketInfo.md) |
| ✅ | `BNET_REQUEST_INVITE_CONFIRMATION` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `BN_BLOCK_FAILED_TOO_MANY` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_BLOCK_LIST_UPDATED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_CHAT_MSG_ADDON` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `BN_CHAT_WHISPER_UNDELIVERABLE` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_CONNECTED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_CUSTOM_MESSAGE_CHANGED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_CUSTOM_MESSAGE_LOADED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_DISCONNECTED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_FRIEND_ACCOUNT_OFFLINE` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_FRIEND_ACCOUNT_ONLINE` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_FRIEND_INFO_CHANGED` | 15 | `-` / `n` | [FriendList](systems/FriendList.md) |
| ✅ | `BN_FRIEND_INVITE_ADDED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_FRIEND_INVITE_LIST_INITIALIZED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_FRIEND_INVITE_REMOVED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_FRIEND_LIST_SIZE_CHANGED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_INFO_CHANGED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `BN_REQUEST_FOF_SUCCEEDED` |  |  | [FriendList](systems/FriendList.md) |
| ⛔ | `BN_WHISPER` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `BONUS_ROLL_ACTIVATE` |  |  | [Loot](systems/Loot.md) |
| ✅ | `BONUS_ROLL_DEACTIVATE` |  |  | [Loot](systems/Loot.md) |
| ✅ | `BONUS_ROLL_FAILED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `BONUS_ROLL_RESULT` |  |  | [Loot](systems/Loot.md) |
| ✅ | `BONUS_ROLL_STARTED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `BOSS_KILL` |  |  | [EncounterInfo](systems/EncounterInfo.md) |
| ✅ | `BULK_PURCHASE_RESULT_RECEIVED` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `BULK_REFUND_RESULT_RECEIVED` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ⛔ | `BUYOUT_AUCTION` |  |  | used in `Blizzard_AuctionHouseUI/Shared/Blizzard_AuctionHouseFrame.lua` |
| ✅ | `B_NET_NEIGHBORHOOD_LIST_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `CALENDAR_ACTION_PENDING` | 1 | `b` | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_CLOSE_EVENT` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_EVENT_ALARM` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_NEW_EVENT` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_OPEN_EVENT` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_UPDATE_ERROR` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_UPDATE_ERROR_WITH_COUNT` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_UPDATE_ERROR_WITH_PLAYER_NAME` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_UPDATE_EVENT` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_UPDATE_EVENT_LIST` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_UPDATE_GUILD_EVENTS` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_UPDATE_INVITE_LIST` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CALENDAR_UPDATE_PENDING_INVITES` |  |  | [Calendar](systems/Calendar.md) |
| ✅ | `CANCEL_ALL_LOOT_ROLLS` |  |  | [Loot](systems/Loot.md) |
| ⛔ | `CANCEL_AUCTION` |  |  | used in `Blizzard_AuctionHouseUI/Shared/Blizzard_AuctionHouseFrame.lua` |
| ✅ | `CANCEL_GLYPH_CAST` |  |  | [GlyphInfo](systems/GlyphInfo.md) |
| ✅ | `CANCEL_LOOT_ROLL` |  |  | [Loot](systems/Loot.md) |
| ✅ | `CANCEL_NEIGHBORHOOD_INVITE_RESPONSE` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `CANCEL_PLAYER_COUNTDOWN` |  |  | [WorldStateInfo](systems/WorldStateInfo.md) |
| ✅ | `CANCEL_SUMMON` |  |  | [Unit](systems/Unit.md) |
| ⛔ | `CANNOT_RUN_ANY_CHILD_DUNGEON` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ✅ | `CAN_LOCAL_WHISPER_TARGET_RESPONSE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CAN_PLAYER_SPEAK_LANGUAGE_CHANGED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CAPTUREFRAMES_FAILED` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `CAPTUREFRAMES_SUCCEEDED` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `CATALOG_SHOP_ADD_PENDING_PRODUCT` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_DATA_REFRESH` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_DISABLED` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_FETCH_FAILURE` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_FETCH_SUCCESS` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_OPEN_SIMPLE_CHECKOUT` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_PURCHASE_SUCCESS` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_REBUILD_SCROLL_BOX` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_REFUNDABLE_DECORS_UPDATED` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_REMOVE_PENDING_PRODUCT` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_RESULT_ERROR` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_SPECIFIC_PRODUCT_REFRESH` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_VIRTUAL_CURRENCY_BALANCE_UPDATE` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CATALOG_SHOP_VIRTUAL_CURRENCY_BALANCE_UPDATE_FAILURE` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `CAUTIONARY_CHANNEL_MESSAGE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CAUTIONARY_CHAT_MESSAGE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CEMETERY_PREFERENCE_UPDATED` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `CHALLENGE_MODE_COMPLETED` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_COMPLETED_REWARDS` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_DEATH_COUNT_UPDATED` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_KEYSTONE_RECEPTABLE_OPEN` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_KEYSTONE_SLOTTED` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_LEADERBOARD_RESULT` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_LEADERS_UPDATE` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_LEAVER_TIMER_ENDED` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_LEAVER_TIMER_STARTED` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_MAPS_UPDATE` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_MEMBER_INFO_UPDATED` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_NEW_RECORD` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_RESET` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHALLENGE_MODE_START` |  |  | [ChallengeModeInfo](systems/ChallengeModeInfo.md) |
| ✅ | `CHANNEL_COUNT_UPDATE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHANNEL_FLAGS_UPDATED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHANNEL_INVITE_REQUEST` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHANNEL_LEFT` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHANNEL_PASSWORD_REQUEST` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHANNEL_ROSTER_UPDATE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHANNEL_UI_UPDATE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| 🆕 | `CHARACTER_COPY_STATUS_CHANGED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `CHARACTER_CREATION_RESULT` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| 🆕 | `CHARACTER_DECLINE_IN_PROGRESS` |  |  | used in `Blizzard_DeclensionFrame/Camelot/DeclensionFrameGlue.lua` |
| 🆕 | `CHARACTER_DECLINE_RESULT` |  |  | used in `Blizzard_DeclensionFrame/Camelot/DeclensionFrameGlue.lua` |
| 🆕 | `CHARACTER_DELETION_RESULT` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `CHARACTER_DUPLICATE_LOGON` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `CHARACTER_ITEM_FIXUP_NOTIFICATION` |  |  | [Item](systems/Item.md) |
| 🆕 | `CHARACTER_LIST_GROUP_CREATED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectList.lua` |
| 🆕 | `CHARACTER_LIST_GROUP_DELETED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectList.lua` |
| 🆕 | `CHARACTER_LIST_MAIL_RECEIVED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectUI.lua` |
| 🆕 | `CHARACTER_LIST_RESTRICTIONS_RECEIVED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectList.lua` |
| 🆕 | `CHARACTER_LIST_RETRIEVAL_RESULT` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `CHARACTER_LIST_RETRIEVING` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `CHARACTER_LIST_UPDATE` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `CHARACTER_POINTS_CHANGED` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| 🆕 | `CHARACTER_UNDELETE_FINISHED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `CHARACTER_UNDELETE_STARTED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `CHARACTER_UNDELETE_STATUS_CHANGED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `CHARACTER_UPGRADE_SPELL_TIER_SET` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| 🆕 | `CHARACTER_UPGRADE_UNREVOKE_RESULT` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ⛔ | `CHARGE` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| 🆕 | `CHAR_CREATE_ANIM_KIT_FINISHED` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| 🆕 | `CHAR_CREATE_BACKGROUND_MODEL_READY` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| 🆕 | `CHAR_CREATE_BEGIN_ANIMATIONS` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| 🆕 | `CHAR_RENAME_IN_PROGRESS` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `CHAR_RESTORE_COMPLETE` |  |  | used in `Blizzard_GlueXML/Camelot/CharacterCopy.lua` |
| 🆕 | `CHAR_SELECT_BACKGROUND_MODEL_READY` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectUI.lua` |
| ✅ | `CHAT_COMBAT_MSG_ARENA_POINTS_GAIN` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_DISABLED_CHANGED` |  |  | [SocialRestrictions](systems/SocialRestrictions.md) |
| ✅ | `CHAT_DISABLED_CHANGE_FAILED` |  |  | [SocialRestrictions](systems/SocialRestrictions.md) |
| ✅ | `CHAT_LOGGING_CHANGED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_ACHIEVEMENT` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_ADDON` | 16 | `s,s,s,s,s,n,n,s,n` | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_ADDON_LOGGED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_AFK` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BG_SYSTEM_ALLIANCE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BG_SYSTEM_HORDE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BG_SYSTEM_NEUTRAL` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BN` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BN_INLINE_TOAST_ALERT` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BN_INLINE_TOAST_BROADCAST` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BN_INLINE_TOAST_BROADCAST_INFORM` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BN_INLINE_TOAST_CONVERSATION` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BN_WHISPER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BN_WHISPER_INFORM` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_BN_WHISPER_PLAYER_OFFLINE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_CHANNEL` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_CHANNEL_JOIN` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_CHANNEL_LEAVE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_CHANNEL_LEAVE_PREVENTED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_CHANNEL_LIST` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_CHANNEL_NOTICE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_CHANNEL_NOTICE_USER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_COLLECTED_APPEARANCE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_COMBAT_FACTION_CHANGE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_COMBAT_HONOR_GAIN` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_COMBAT_MISC_INFO` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_COMBAT_XP_GAIN` | 1 | `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t` | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_COMMUNITIES_CHANNEL` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_CURRENCY` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_DND` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_EMOTE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_FILTERED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_GUILD` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_GUILD_ACHIEVEMENT` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_GUILD_DISCORD` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_GUILD_ITEM_LOOTED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_IGNORED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_INSTANCE_CHAT` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_INSTANCE_CHAT_LEADER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_LOOT` | 2 | `s,s,s,s,s,s,n,n,s,n,n,s,n,b,b,b,b,t` | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_MONEY` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_MONSTER_EMOTE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_MONSTER_PARTY` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_MONSTER_SAY` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_MONSTER_WHISPER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_MONSTER_YELL` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_OFFICER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_OPENING` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_PARTY` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_PARTY_LEADER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_PET_BATTLE_COMBAT_LOG` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_PET_BATTLE_INFO` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_PET_INFO` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_PING` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_RAID` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_RAID_BOSS_EMOTE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_RAID_BOSS_WHISPER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_RAID_LEADER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_RAID_WARNING` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_RESTRICTED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_SAY` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_SKILL` | 1 | `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t` | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_SYSTEM` | 1 | `s,s,s,s,s,s,n,n,s,n,n,-,n,b,b,b,b,t` | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_TARGETICONS` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_TEXT_EMOTE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_TRADESKILLS` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_VOICE_TEXT` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_WHISPER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_WHISPER_INFORM` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_MSG_YELL` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_REGIONAL_SEND_FAILED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_REGIONAL_STATUS_CHANGED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_SERVER_DISCONNECTED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CHAT_SERVER_RECONNECTED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| 🆕 | `CHECK_CHARACTER_NAME_AVAILABILITY_RESULT` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| ⛔ | `CHEER` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `CHEST_REWARDS_UPDATED_FROM_SERVER` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ⛔ | `CHICKEN` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `CINEMATIC_START` |  |  | [Cinematic](systems/Cinematic.md) |
| ✅ | `CINEMATIC_STOP` |  |  | [Cinematic](systems/Cinematic.md) |
| ⛔ | `CLASS_TALENTS_SWITCH_TO_LOADOUT_BY_INDEX` |  |  | [ClassTalents](systems/ClassTalents.md) |
| ⛔ | `CLASS_TALENTS_SWITCH_TO_LOADOUT_BY_NAME` |  |  | [ClassTalents](systems/ClassTalents.md) |
| ⛔ | `CLASS_TALENTS_SWITCH_TO_SPECIALIZATION_BY_INDEX` |  |  | [ClassTalents](systems/ClassTalents.md) |
| ⛔ | `CLASS_TALENTS_SWITCH_TO_SPECIALIZATION_BY_NAME` |  |  | [ClassTalents](systems/ClassTalents.md) |
| ✅ | `CLASS_TRIAL_TIMER_START` |  |  | [ClassTrial](systems/ClassTrial.md) |
| ✅ | `CLASS_TRIAL_UPGRADE_COMPLETE` |  |  | [ClassTrial](systems/ClassTrial.md) |
| ✅ | `CLEAR_BOSS_EMOTES` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `CLICKBINDINGS_SET_HIGHLIGHTS_SHOWN` |  |  | [ClickBindings](systems/ClickBindings.md) |
| 🆕 | `CLIENT_FEATURE_STATUS_CHANGED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `CLIENT_SCENE_CLOSED` |  |  | [ClientScene](systems/ClientScene.md) |
| ✅ | `CLIENT_SCENE_OPENED` |  |  | [ClientScene](systems/ClientScene.md) |
| ✅ | `CLOSE_CHARTER_CONFIRMATION_UI` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `CLOSE_CREATE_CHARTER_NEIGHBORHOOD_UI` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `CLOSE_CREATE_GUILD_NEIGHBORHOOD_UI` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `CLOSE_INBOX_ITEM` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `CLOSE_PLOT_CORNERSTONE` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `CLOSE_TABARD_FRAME` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `CLUB_ADDED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_ERROR` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_FINDER_APPLICANT_INVITE_RECIEVED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_APPLICATIONS_UPDATED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_CAN_WHISPER_APPLICANT` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_CLUB_LIST_RETURNED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_CLUB_REPORTED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_COMMUNITY_OFFLINE_JOIN` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_ENABLED_OR_DISABLED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_GUILD_REALM_NAME_UPDATED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_LINKED_CLUB_RETURNED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_MEMBERSHIP_LIST_CHANGED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_PLAYER_PENDING_LIST_RECIEVED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_POST_UPDATED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_RECRUITMENT_POST_RETURNED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_RECRUITS_UPDATED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_FINDER_RECRUIT_LIST_CHANGED` |  |  | [ClubFinderInfo](systems/ClubFinderInfo.md) |
| ✅ | `CLUB_INVITATIONS_RECEIVED_FOR_CLUB` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_INVITATION_ADDED_FOR_SELF` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_INVITATION_REMOVED_FOR_SELF` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_MEMBERS_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_MEMBER_ADDED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_MEMBER_PRESENCE_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_MEMBER_REMOVED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_MEMBER_ROLE_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_MEMBER_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_MESSAGE_ADDED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_MESSAGE_HISTORY_RECEIVED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_MESSAGE_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_REMOVED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_REMOVED_MESSAGE` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_SELF_MEMBER_ROLE_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_STREAMS_LOADED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_STREAM_ADDED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_STREAM_REMOVED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_STREAM_SUBSCRIBED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_STREAM_UNSUBSCRIBED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_STREAM_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_TICKETS_RECEIVED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_TICKET_CREATED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_TICKET_RECEIVED` |  |  | [Club](systems/Club.md) |
| ✅ | `CLUB_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `COLOR_OVERRIDES_RESET` |  |  | [ColorOverrides](systems/ColorOverrides.md) |
| ✅ | `COLOR_OVERRIDE_UPDATED` |  |  | [ColorOverrides](systems/ColorOverrides.md) |
| ⛔ | `COMBAT_LOG_APPLY_FILTER_SETTINGS` |  |  | [CombatLogSecure](systems/CombatLogSecure.md) |
| ✅ | `COMBAT_LOG_ENTRIES_CLEARED` |  |  | [CombatLog](systems/CombatLog.md) |
| ✅ | `COMBAT_LOG_EVENT` |  |  | [CombatLog](systems/CombatLog.md) |
| ⛔ | `COMBAT_LOG_EVENT_INTERNAL_UNFILTERED` |  |  | [CombatLogInternal](systems/CombatLogInternal.md) |
| ✅ | `COMBAT_LOG_EVENT_UNFILTERED` |  |  | [CombatLog](systems/CombatLog.md) |
| ✅ | `COMBAT_LOG_MESSAGE` | 300 | `s,n,n,n,n` | [CombatLogSecure](systems/CombatLogSecure.md) |
| ✅ | `COMBAT_LOG_MESSAGE_LIMIT_CHANGED` |  |  | [CombatLog](systems/CombatLog.md) |
| ⛔ | `COMBAT_LOG_REFILTER_ENTRIES` |  |  | [CombatLogSecure](systems/CombatLogSecure.md) |
| ✅ | `COMBAT_RATING_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `COMBAT_TEXT_UPDATE` |  |  | [CombatText](systems/CombatText.md) |
| ✅ | `COMBO_TARGET_CHANGED` | 2 | `` | [Unit](systems/Unit.md) |
| ✅ | `COMMENTATOR_COMBAT_EVENT` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMENTATOR_ENTER_WORLD` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMENTATOR_HISTORY_FLUSHED` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMENTATOR_IMMEDIATE_FOV_UPDATE` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMENTATOR_MAP_UPDATE` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMENTATOR_PLAYER_NAME_OVERRIDE_UPDATE` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMENTATOR_PLAYER_UPDATE` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMENTATOR_RESET_SETTINGS` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMENTATOR_TEAMS_SWAPPED` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMENTATOR_TEAM_NAME_UPDATE` |  |  | [CommentatorFrame](systems/CommentatorFrame.md) |
| ✅ | `COMMODITY_PRICE_UNAVAILABLE` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `COMMODITY_PRICE_UPDATED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `COMMODITY_PURCHASED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `COMMODITY_PURCHASE_FAILED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `COMMODITY_PURCHASE_SUCCEEDED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `COMMODITY_SEARCH_RESULTS_ADDED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `COMMODITY_SEARCH_RESULTS_RECEIVED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `COMMODITY_SEARCH_RESULTS_UPDATED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `COMPACT_UNIT_FRAME_PROFILES_LOADED` | 1 | `` | [CompactUnitFrames](systems/CompactUnitFrames.md) |
| ✅ | `COMPANION_LEARNED` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `COMPANION_UNLEARNED` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `COMPANION_UPDATE` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `CONFIG_COMMIT_FAILED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `CONFIRM_BATTLE_NET_FRIEND_INVITE_SHOW` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `CONFIRM_BEFORE_USE` |  |  | [Item](systems/Item.md) |
| ✅ | `CONFIRM_BINDER` |  |  | [Unit](systems/Unit.md) |
| ⛔ | `CONFIRM_BUY_OUTFIT_SLOT` |  |  | used in `Blizzard_Transmog/Blizzard_Transmog.lua` |
| ⛔ | `CONFIRM_DELETE_TRANSMOG_CUSTOM_SET` |  |  | used in `Blizzard_FrameXML/WardrobeCustomSets.lua` |
| ⛔ | `CONFIRM_DESTROY_COMMUNITY` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ⛔ | `CONFIRM_DESTROY_COMMUNITY_STREAM` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ✅ | `CONFIRM_DISENCHANT_ROLL` |  |  | [Loot](systems/Loot.md) |
| ⛔ | `CONFIRM_LEAVE_AND_DESTROY_COMMUNITY` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ⛔ | `CONFIRM_LEAVE_COMMUNITY` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ✅ | `CONFIRM_LOOT_ROLL` |  |  | [Loot](systems/Loot.md) |
| ✅ | `CONFIRM_PET_UNLEARN` |  |  | [SpecializationInfo](systems/SpecializationInfo.md) |
| ⛔ | `CONFIRM_REMOVE_COMMUNITY_MEMBER` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ⛔ | `CONFIRM_SAVE_TRANSMOG_CUSTOM_SET` |  |  | used in `Blizzard_FrameXML/WardrobeCustomSets.lua` |
| ✅ | `CONFIRM_SUMMON` |  |  | [Unit](systems/Unit.md) |
| ✅ | `CONFIRM_TALENT_WIPE` |  |  | [SpecializationInfo](systems/SpecializationInfo.md) |
| ⛔ | `CONFIRM_TRANSMOG_USABLE_DISCOUNT` |  |  | used in `Blizzard_Transmog/Blizzard_Transmog.lua` |
| ✅ | `CONFIRM_XP_LOSS` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ⛔ | `CONGRATULATE` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| 🆕 | `CONNECT_TO_EVENT_REALM_FAILED` |  |  | used in `Blizzard_GlueParent/Mainline/GlueParent.lua` |
| ✅ | `CONSOLE_CLEAR` |  |  | [Console](systems/Console.md) |
| ✅ | `CONSOLE_COLORS_CHANGED` |  |  | [Console](systems/Console.md) |
| ✅ | `CONSOLE_FONT_SIZE_CHANGED` |  |  | [Console](systems/Console.md) |
| ✅ | `CONSOLE_LOG` |  |  | [Console](systems/Console.md) |
| ✅ | `CONSOLE_MESSAGE` | 58 | `s,n` | [Console](systems/Console.md) |
| ✅ | `CONTENT_TRACKING_IS_ENABLED_UPDATE` |  |  | [ContentTracking](systems/ContentTracking.md) |
| ✅ | `CONTENT_TRACKING_LIST_UPDATE` | 1 | `` | [ContentTracking](systems/ContentTracking.md) |
| ✅ | `CONTENT_TRACKING_UPDATE` |  |  | [ContentTracking](systems/ContentTracking.md) |
| ✅ | `CONTRIBUTION_CHANGED` |  |  | [ContributionCollector](systems/ContributionCollector.md) |
| ✅ | `CONTRIBUTION_COLLECTOR_PENDING` |  |  | [ContributionCollector](systems/ContributionCollector.md) |
| ✅ | `CONTRIBUTION_COLLECTOR_UPDATE` |  |  | [ContributionCollector](systems/ContributionCollector.md) |
| ✅ | `CONTRIBUTION_COLLECTOR_UPDATE_SINGLE` |  |  | [ContributionCollector](systems/ContributionCollector.md) |
| ✅ | `CONVERT_TO_BIND_TO_ACCOUNT_CONFIRM` |  |  | [Item](systems/Item.md) |
| ✅ | `CONVERT_TO_RAID_CONFIRMATION` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `COOLDOWN_VIEWER_DATA_LOADED` | 1 | `` | [CooldownViewer](systems/CooldownViewer.md) |
| ✅ | `COOLDOWN_VIEWER_SPELL_OVERRIDE_UPDATED` |  |  | [CooldownViewer](systems/CooldownViewer.md) |
| ✅ | `COOLDOWN_VIEWER_TABLE_HOTFIXED` |  |  | [CooldownViewer](systems/CooldownViewer.md) |
| ✅ | `CORPSE_IN_INSTANCE` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `CORPSE_IN_RANGE` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `CORPSE_OUT_OF_RANGE` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `COVENANT_CALLINGS_UPDATED` |  |  | [CovenantCallings](systems/CovenantCallings.md) |
| ✅ | `COVENANT_CHOSEN` |  |  | [Covenant](systems/Covenant.md) |
| ⛔ | `COVENANT_MISSIONS_CONFIRM_ADVENTURE` |  |  | used in `Blizzard_GarrisonUI/Mainline/Blizzard_CovenantMissionUI.lua` |
| ⛔ | `COVENANT_MISSIONS_HEAL_CONFIRMATION` |  |  | used in `Blizzard_GarrisonUI/Mainline/Blizzard_CovenantMissionUI.lua` |
| ✅ | `COVENANT_PREVIEW_CLOSE` |  |  | [CovenantPreview](systems/CovenantPreview.md) |
| ✅ | `COVENANT_PREVIEW_OPEN` |  |  | [CovenantPreview](systems/CovenantPreview.md) |
| ✅ | `COVENANT_RENOWN_CATCH_UP_STATE_UPDATE` |  |  | [CovenantSanctumUI](systems/CovenantSanctumUI.md) |
| ✅ | `COVENANT_SANCTUM_RENOWN_LEVEL_CHANGED` |  |  | [CovenantSanctumUI](systems/CovenantSanctumUI.md) |
| ✅ | `CRAFTINGORDERS_CAN_REQUEST` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_CLAIMED_ORDER_ADDED` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_CLAIMED_ORDER_REMOVED` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_CLAIMED_ORDER_UPDATED` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_CLAIM_ORDER_RESPONSE` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_CRAFT_ORDER_RESPONSE` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_CUSTOMER_FAVORITES_CHANGED` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_CUSTOMER_OPTIONS_PARSED` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_DISPLAY_CRAFTER_FULFILLED_MSG` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_FULFILL_ORDER_RESPONSE` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_HIDE_CRAFTER` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_HIDE_CUSTOMER` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_ORDER_CANCEL_RESPONSE` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_ORDER_PLACEMENT_RESPONSE` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_REJECT_ORDER_RESPONSE` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_RELEASE_ORDER_RESPONSE` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_SHOW_CRAFTER` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_SHOW_CUSTOMER` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_UNEXPECTED_ERROR` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_UPDATE_CUSTOMER_NAME` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_UPDATE_ORDER_COUNT` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_UPDATE_PERSONAL_ORDER_COUNTS` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTINGORDERS_UPDATE_REWARDS` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CRAFTING_DETAILS_UPDATE` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `CRAFTING_HOUSE_DISABLED` |  |  | [CraftingOrderUI](systems/CraftingOrderUI.md) |
| ✅ | `CREATE_NEIGHBORHOOD_RESULT` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `CRITERIA_COMPLETE` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `CRITERIA_EARNED` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `CRITERIA_UPDATE` | 5 | `` | [AchievementInfo](systems/AchievementInfo.md) |
| ⛔ | `CURRENCY` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `CURRENCY_DISPLAY_UPDATE` | 1 | `-,-,-,-,-` | [CurrencySystem](systems/CurrencySystem.md) |
| ✅ | `CURRENCY_TRANSFER_FAILED` |  |  | [CurrencySystem](systems/CurrencySystem.md) |
| ✅ | `CURRENCY_TRANSFER_INITIATED` |  |  | [CurrencySystem](systems/CurrencySystem.md) |
| ✅ | `CURRENCY_TRANSFER_LOG_UPDATE` |  |  | [CurrencySystem](systems/CurrencySystem.md) |
| ✅ | `CURRENCY_TRANSFER_SUCCESS` |  |  | [CurrencySystem](systems/CurrencySystem.md) |
| ✅ | `CURRENT_HOUSE_INFO_RECIEVED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `CURRENT_HOUSE_INFO_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `CURRENT_SPELL_CAST_CHANGED` | 52 | `b` | [SpellBook](systems/SpellBook.md) |
| ✅ | `CURSOR_CHANGED` | 15 | `b,n,n,n` | [Cursor](systems/Cursor.md) |
| 🆕 | `CUSTOMIZE_CHARACTER_RESULT` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| 🆕 | `CUSTOMIZE_CHARACTER_STARTED` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| ⛔ | `CUSTOM_SET_INVALID_NAME` |  |  | used in `Blizzard_FrameXML/WardrobeCustomSets.lua` |
| ✅ | `CVAR_UPDATE` | 9 | `s,s` | [Console](systems/Console.md) |
| ✅ | `DAILY_RESET_INSTANCE_WELCOME` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `DAMAGE_METER_COMBAT_SESSION_UPDATED` | 182 | `n,n` | [DamageMeter](systems/DamageMeter.md) |
| ✅ | `DAMAGE_METER_CURRENT_SESSION_UPDATED` | 1 | `` | [DamageMeter](systems/DamageMeter.md) |
| ✅ | `DAMAGE_METER_RESET` |  |  | [DamageMeter](systems/DamageMeter.md) |
| ⛔ | `DANCE` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ⛔ | `DEATHKNIGHT` |  |  | used in `Blizzard_FrameXMLBase/Cata/Constants.lua` |
| 🆕 | `DEBUG_MAP_OBJECTS_UPDATED` |  |  | used in `Blizzard_WorldMap/WM_DebugDataProvider.lua` |
| 🆕 | `DEBUG_MENU_TOGGLED` |  |  | used in `Blizzard_Console/Blizzard_Console.lua` |
| 🆕 | `DEBUG_PORT_LOCS_UPDATED` |  |  | used in `Blizzard_WorldMap/WM_DebugDataProvider.lua` |
| ✅ | `DECLINE_NEIGHBORHOOD_INVITATION_RESPONSE` |  |  | [HousingUI](systems/HousingUI.md) |
| 🆕 | `DELETED_CHARACTER_LIST_RETRIEVAL_RESULT` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `DELETED_CHARACTER_LIST_RETRIEVING` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `DELETE_ITEM_CONFIRM` |  |  | [Item](systems/Item.md) |
| ✅ | `DELVES_ACCOUNT_DATA_ELEMENT_CHANGED` |  |  | [DelvesUI](systems/DelvesUI.md) |
| ✅ | `DELVE_ASSIST_ACTION` |  |  | [DelvesUI](systems/DelvesUI.md) |
| ⛔ | `DEMONHUNTER` |  |  | used in `Blizzard_FrameXMLBase/Mainline/Constants.lua` |
| ✅ | `DIEL_CYCLE_CHANGED` |  |  | [DateAndTime](systems/DateAndTime.md) |
| ✅ | `DISABLE_DECLINE_GUILD_INVITE` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `DISABLE_LOW_LEVEL_RAID` |  |  | [EncounterInfo](systems/EncounterInfo.md) |
| ✅ | `DISABLE_TAXI_BENCHMARK` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `DISABLE_XP_GAIN` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `DISCORD_GUILD_ACHIEVEMENT` |  |  | [Discord](systems/Discord.md) |
| ✅ | `DISCORD_GUILD_LOBBY_UPDATE` |  |  | [Discord](systems/Discord.md) |
| ✅ | `DISCORD_GUILD_SETTINGS_UPDATE` |  |  | [Discord](systems/Discord.md) |
| ✅ | `DISCORD_LINK_UPDATE` |  |  | [Discord](systems/Discord.md) |
| ✅ | `DISCORD_SERVER_LIST_UPDATE` |  |  | [Discord](systems/Discord.md) |
| ✅ | `DISCORD_STATUS_UPDATE` |  |  | [Discord](systems/Discord.md) |
| ✅ | `DISPLAY_EVENT_TOASTS` |  |  | [UIEventToastManagerInfo](systems/UIEventToastManagerInfo.md) |
| ✅ | `DISPLAY_EVENT_TOAST_LINK` |  |  | [UIEventToastManagerInfo](systems/UIEventToastManagerInfo.md) |
| 🆕 | `DISPLAY_PROMOTION` |  |  | used in `Blizzard_GlueXML/PromotionFrame.lua` |
| ✅ | `DISPLAY_SIZE_CHANGED` | 2 | `` | [Video](systems/Video.md) |
| ⛔ | `DRUID` |  |  | used in `Blizzard_FrameXMLBase/Camelot/Constants.lua` |
| ✅ | `DUEL_FINISHED` |  |  | [DuelInfo](systems/DuelInfo.md) |
| ✅ | `DUEL_INBOUNDS` |  |  | [DuelInfo](systems/DuelInfo.md) |
| ✅ | `DUEL_OUTOFBOUNDS` |  |  | [DuelInfo](systems/DuelInfo.md) |
| ✅ | `DUEL_REQUESTED` |  |  | [DuelInfo](systems/DuelInfo.md) |
| ✅ | `DUEL_TO_THE_DEATH_REQUESTED` |  |  | [DuelInfo](systems/DuelInfo.md) |
| ✅ | `DYE_COLOR_CATEGORY_UPDATED` |  |  | [DyeColorInfo](systems/DyeColorInfo.md) |
| ✅ | `DYE_COLOR_UPDATED` |  |  | [DyeColorInfo](systems/DyeColorInfo.md) |
| 🆕 | `DYNAMIC_BUNDLE_PRICE_UPDATED` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| ✅ | `DYNAMIC_GOSSIP_POI_UPDATED` |  |  | [GossipInfo](systems/GossipInfo.md) |
| ✅ | `ECLIPSE_DIRECTION_CHANGE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `EDIT_MODE_LAYOUTS_UPDATED` | 1 | `t,b` | [EditModeManager](systems/EditModeManager.md) |
| ✅ | `EJ_DIFFICULTY_UPDATE` |  |  | [EncounterJournal](systems/EncounterJournal.md) |
| ✅ | `EJ_LOOT_DATA_RECIEVED` |  |  | [EncounterJournal](systems/EncounterJournal.md) |
| ⛔ | `EMOTE` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `ENABLE_DECLINE_GUILD_INVITE` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `ENABLE_LOW_LEVEL_RAID` |  |  | [EncounterInfo](systems/EncounterInfo.md) |
| ✅ | `ENABLE_TAXI_BENCHMARK` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `ENABLE_XP_GAIN` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `ENCHANT_SPELL_COMPLETED` |  |  | [Spell](systems/Spell.md) |
| ✅ | `ENCHANT_SPELL_SELECTED` |  |  | [Spell](systems/Spell.md) |
| ✅ | `ENCOUNTER_END` |  |  | [EncounterInfo](systems/EncounterInfo.md) |
| ⛔ | `ENCOUNTER_EVENT` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `ENCOUNTER_LOOT_RECEIVED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `ENCOUNTER_START` |  |  | [EncounterInfo](systems/EncounterInfo.md) |
| ✅ | `ENCOUNTER_STATE_CHANGED` |  |  | [InstanceEncounter](systems/InstanceEncounter.md) |
| ✅ | `ENCOUNTER_TIMELINE_EVENT_ADDED` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_EVENT_BLOCK_STATE_CHANGED` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_EVENT_COLOR_CHANGED` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_EVENT_HIGHLIGHT` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_EVENT_REMOVED` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_EVENT_STATE_CHANGED` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_EVENT_TRACK_CHANGED` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_LAYOUT_UPDATED` | 1 | `` | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_STATE_UPDATED` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_VIEW_ACTIVATED` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_TIMELINE_VIEW_DEACTIVATED` |  |  | [EncounterTimeline](systems/EncounterTimeline.md) |
| ✅ | `ENCOUNTER_WARNING` |  |  | [EncounterWarnings](systems/EncounterWarnings.md) |
| ✅ | `END_BOUND_TRADEABLE` |  |  | [Item](systems/Item.md) |
| ⛔ | `ENGAGED_IN_PVP` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ✅ | `ENTERED_DIFFERENT_INSTANCE_FROM_PARTY` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `ENTITLEMENT_DELIVERED` |  |  | [WowEntitlementInfo](systems/WowEntitlementInfo.md) |
| ✅ | `EQUIPMENT_SETS_CHANGED` |  |  | [EquipmentSet](systems/EquipmentSet.md) |
| ✅ | `EQUIPMENT_SWAP_FINISHED` |  |  | [EquipmentSet](systems/EquipmentSet.md) |
| ✅ | `EQUIPMENT_SWAP_PENDING` |  |  | [EquipmentSet](systems/EquipmentSet.md) |
| ✅ | `EQUIP_BIND_CONFIRM` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `EQUIP_BIND_REFUNDABLE_CONFIRM` |  |  | [Container](systems/Container.md) |
| ✅ | `EQUIP_BIND_TRADEABLE_CONFIRM` |  |  | [Container](systems/Container.md) |
| ✅ | `EVENT_REALM_QUEUES_UPDATED` |  |  | [GameRules](systems/GameRules.md) |
| ✅ | `EVENT_SCHEDULER_UPDATE` | 1 | `` | [EventSchedulerUI](systems/EventSchedulerUI.md) |
| ⛔ | `EVOKER` |  |  | used in `Blizzard_FrameXMLBase/Mainline/Constants.lua` |
| ✅ | `EXPAND_BAG_BAR_CHANGED` |  |  | [Container](systems/Container.md) |
| ⛔ | `EXPANSION_TOO_LOW` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| 🆕 | `EXPERIMENTAL_CVAR_CONFIRMATION_NEEDED` | 1 | `` |  |
| ✅ | `EXTERNAL_EVENT_LAUNCH_URL_RESULT` |  |  | [ExternalEventURL](systems/ExternalEventURL.md) |
| ✅ | `EXTERNAL_EVENT_URL_CHANGED` |  |  | [ExternalEventURL](systems/ExternalEventURL.md) |
| ✅ | `EXTRA_BROWSE_INFO_RECEIVED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `FACTION_STANDING_CHANGED` |  |  | [ReputationInfo](systems/ReputationInfo.md) |
| ✅ | `FIRST_FRAME_RENDERED` | 1 | `` | [SystemInfo](systems/SystemInfo.md) |
| ⛔ | `FLIRT` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `FOG_OF_WAR_UPDATED` |  |  | [FogOfWar](systems/FogOfWar.md) |
| ⛔ | `FOLLOW` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `FORBIDDEN_NAME_PLATE_CREATED` |  |  | [NamePlateManager](systems/NamePlateManager.md) |
| ✅ | `FORBIDDEN_NAME_PLATE_UNIT_ADDED` |  |  | [NamePlateManager](systems/NamePlateManager.md) |
| ✅ | `FORBIDDEN_NAME_PLATE_UNIT_REMOVED` |  |  | [NamePlateManager](systems/NamePlateManager.md) |
| 🆕 | `FORCE_DECLINE_CHARACTER` |  |  | used in `Blizzard_DeclensionFrame/Camelot/DeclensionFrameGlue.lua` |
| ✅ | `FORCE_REFRESH_HOUSE_FINDER` |  |  | [HousingUI](systems/HousingUI.md) |
| 🆕 | `FORCE_RENAME_CHARACTER` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `FRAMESTACK_VISIBILITY_UPDATED` |  |  | used in `Blizzard_DebugTools/Blizzard_DebugTools.lua` |
| 🆕 | `FRAMES_LOADED` |  |  | used in `Blizzard_FriendsFrame/Camelot/FriendsFrame.lua` |
| ✅ | `FRAME_MANAGER_UPDATE_ALL` |  |  | [UIFrameManager](systems/UIFrameManager.md) |
| ✅ | `FRAME_MANAGER_UPDATE_FRAME` |  |  | [UIFrameManager](systems/UIFrameManager.md) |
| ✅ | `FRIENDLIST_UPDATE` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `FULLSCREEN_BROWSER_SPINNER_HIDE` |  |  | [Browser](systems/Browser.md) |
| ✅ | `FULLSCREEN_BROWSER_SPINNER_SHOW` |  |  | [Browser](systems/Browser.md) |
| ✅ | `GAMEPAD_POSSESS_BAR_OVERRIDE_CHANGED` |  |  | [GamepadUI](systems/GamepadUI.md) |
| ✅ | `GAMEPAD_STANCE_BAR_OVERRIDE_CHANGED` |  |  | [GamepadUI](systems/GamepadUI.md) |
| ✅ | `GAME_MODE_DISPLAY_INFO_UPDATED` |  |  | [GameRules](systems/GameRules.md) |
| ✅ | `GAME_MODE_DISPLAY_MODE_TOGGLE_DISABLED` |  |  | [GameRules](systems/GameRules.md) |
| ✅ | `GAME_PAD_ACTIVE_CHANGED` |  |  | [GamePad](systems/GamePad.md) |
| ✅ | `GAME_PAD_ALLOW_HOVER_EVENTS_WITH_FREE_LOOK_CHANGED` |  |  | [GamePad](systems/GamePad.md) |
| ✅ | `GAME_PAD_CONFIGS_CHANGED` | 1 | `` | [GamePad](systems/GamePad.md) |
| ✅ | `GAME_PAD_CONNECTED` |  |  | [GamePad](systems/GamePad.md) |
| ✅ | `GAME_PAD_DISCONNECTED` |  |  | [GamePad](systems/GamePad.md) |
| ✅ | `GAME_PAD_POWER_CHANGED` |  |  | [GamePad](systems/GamePad.md) |
| ✅ | `GAME_RULES_CHANGED` |  |  | [GameRules](systems/GameRules.md) |
| ✅ | `GARRISON_ARCHITECT_CLOSED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_ARCHITECT_OPENED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_BUILDING_ACTIVATABLE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_BUILDING_ACTIVATED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_BUILDING_ERROR` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_BUILDING_LIST_UPDATE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_BUILDING_PLACED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_BUILDING_REMOVED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_BUILDING_UPDATE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_FOLLOWER_ADDED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_FOLLOWER_CATEGORIES_UPDATED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_FOLLOWER_DURABILITY_CHANGED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_FOLLOWER_HEALED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_FOLLOWER_LIST_UPDATE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_FOLLOWER_REMOVED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_FOLLOWER_UPGRADED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_FOLLOWER_XP_CHANGED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_HIDE_LANDING_PAGE` | 1 | `` | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_INVASION_AVAILABLE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_INVASION_UNAVAILABLE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_LANDINGPAGE_SHIPMENTS` | 1 | `` | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MISSION_AREA_BONUS_ADDED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MISSION_BONUS_ROLL_COMPLETE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MISSION_BONUS_ROLL_LOOT` |  |  | [Loot](systems/Loot.md) |
| ✅ | `GARRISON_MISSION_COMPLETE_RESPONSE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MISSION_FINISHED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MISSION_LIST_UPDATE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MISSION_NPC_CLOSED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MISSION_NPC_OPENED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MISSION_REWARD_INFO` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MISSION_STARTED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MONUMENT_CLOSE_UI` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MONUMENT_LIST_LOADED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MONUMENT_REPLACED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MONUMENT_SELECTED_TROPHY_ID_LOADED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_MONUMENT_SHOW_UI` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_RANDOM_MISSION_ADDED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_RECALL_PORTAL_LAST_USED_TIME` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_RECALL_PORTAL_USED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_RECRUITMENT_FOLLOWERS_GENERATED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_RECRUITMENT_NPC_CLOSED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_RECRUITMENT_NPC_OPENED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_RECRUITMENT_READY` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_RECRUIT_FOLLOWER_RESULT` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_SHIPMENT_RECEIVED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_SHIPYARD_NPC_CLOSED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_SHIPYARD_NPC_OPENED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_SHOW_LANDING_PAGE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_SPEC_GROUPS_CLEARED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_SPEC_GROUP_UPDATED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_TALENT_COMPLETE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_TALENT_EVENT_UPDATE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_TALENT_NPC_CLOSED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_TALENT_NPC_OPENED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_TALENT_RESEARCH_STARTED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_TALENT_UNLOCKS_RESULT` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_TALENT_UPDATE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_TRADESKILL_NPC_CLOSED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_UPDATE` | 1 | `` | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_UPGRADEABLE_RESULT` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GARRISON_USE_PARTY_GARRISON_CHANGED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `GDF_SIM_COMPLETE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ⛔ | `GEAR_TOO_HIGH` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ⛔ | `GEAR_TOO_LOW` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ✅ | `GENERIC_ERROR` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `GENERIC_WIDGET_DISPLAY_SHOW` |  |  | [GenericWidgetDisplay](systems/GenericWidgetDisplay.md) |
| ✅ | `GET_ITEM_INFO_RECEIVED` |  |  | [Item](systems/Item.md) |
| ✅ | `GLOBAL_MOUSE_DOWN` | 42 | `s` | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `GLOBAL_MOUSE_UP` | 42 | `s` | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `GLOBAL_REGION_MOUSE_DOWN` | 33 | `-,s` / `t,s` | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `GLOBAL_REGION_MOUSE_UP` | 42 | `-,s` / `t,s` | [SystemInfo](systems/SystemInfo.md) |
| 🆕 | `GLUES_RESUMED` |  |  | used in `Blizzard_MatchmakingQueueDisplay/Blizzard_MatchmakingQueueDisplay.lua` |
| ✅ | `GLUE_SCREENSHOT_FAILED` |  |  | [Video](systems/Video.md) |
| ✅ | `GLUE_SCREENSHOT_STARTED` |  |  | [Video](systems/Video.md) |
| ✅ | `GLUE_SCREENSHOT_SUCCEEDED` |  |  | [Video](systems/Video.md) |
| ✅ | `GM_PLAYER_INFO` |  |  | [GMTicketInfo](systems/GMTicketInfo.md) |
| ✅ | `GOSSIP_CLOSED` |  |  | [GossipInfo](systems/GossipInfo.md) |
| ✅ | `GOSSIP_CONFIRM` |  |  | [GossipInfo](systems/GossipInfo.md) |
| ✅ | `GOSSIP_CONFIRM_CANCEL` |  |  | [GossipInfo](systems/GossipInfo.md) |
| ✅ | `GOSSIP_ENTER_CODE` |  |  | [GossipInfo](systems/GossipInfo.md) |
| ✅ | `GOSSIP_OPTIONS_REFRESHED` |  |  | [GossipInfo](systems/GossipInfo.md) |
| ✅ | `GOSSIP_SHOW` |  |  | [GossipInfo](systems/GossipInfo.md) |
| ✅ | `GROUP_BUFF_VISUAL_ALERTS_CHANGED` | 3 | `t` | [UnitAuras](systems/UnitAuras.md) |
| ✅ | `GROUP_FORMED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `GROUP_INVITE_CONFIRMATION` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `GROUP_JOINED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `GROUP_LEFT` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `GROUP_ROSTER_UPDATE` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ⛔ | `GUILD` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `GUILDBANKBAGSLOTS_CHANGED` |  |  | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDBANKFRAME_CLOSED` |  |  | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDBANKFRAME_OPENED` |  |  | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDBANKLOG_UPDATE` |  |  | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDBANK_ITEM_LOCK_CHANGED` |  |  | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDBANK_TEXT_CHANGED` |  |  | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDBANK_UPDATE_MONEY` |  |  | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDBANK_UPDATE_TABS` |  |  | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDBANK_UPDATE_TEXT` |  |  | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDBANK_UPDATE_WITHDRAWMONEY` | 1 | `` | [GuildBank](systems/GuildBank.md) |
| ✅ | `GUILDTABARD_UPDATE` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ⛔ | `GUILD_ACHIEVEMENT` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `GUILD_CHALLENGE_COMPLETED` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_CHALLENGE_UPDATED` | 1 | `` | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_EVENT_LOG_UPDATE` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_INVITE_CANCEL` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_INVITE_REQUEST` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_MOTD` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_NEWS_UPDATE` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_PARTY_STATE_UPDATED` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_PREFERRED_PLAY_SETTINGS_UPDATED` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_RANKS_UPDATE` | 3 | `` | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_RANKS_UPDATE_ACTIVE_PLAYER` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_RECIPE_KNOWN_BY_MEMBERS` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_REGISTRAR_CLOSED` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_REGISTRAR_SHOW` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_RENAME_NAME_CHECK` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_RENAME_REFUND_RESULT` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_RENAME_REQUIRED` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_RENAME_STATUS_UPDATE` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_REWARDS_LIST` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_REWARDS_LIST_UPDATE` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_ROSTER_UPDATE` | 10 | `b` | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GUILD_TRADESKILL_UPDATE` | 6 | `` | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `GX_RESTARTED` |  |  | [Video](systems/Video.md) |
| ✅ | `HANDLE_UI_ACTION` |  |  | [UIActionHandlerSystem](systems/UIActionHandlerSystem.md) |
| ✅ | `HARDCORE_DEATHS` |  |  | [DeathAlert](systems/DeathAlert.md) |
| ⛔ | `HEALME` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `HEARTHSTONE_BOUND` |  |  | [Unit](systems/Unit.md) |
| ✅ | `HEIRLOOMS_UPDATED` |  |  | [HeirloomInfo](systems/HeirloomInfo.md) |
| ✅ | `HEIRLOOM_UPGRADE_TARGETING_CHANGED` |  |  | [HeirloomInfo](systems/HeirloomInfo.md) |
| ⛔ | `HELLO` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ⛔ | `HELPME` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `HIDDEN_GROUP_BUFFS_CHANGED` | 3 | `t` | [UnitAuras](systems/UnitAuras.md) |
| 🆕 | `HIDE_ARROW_CALLOUT` |  |  | used in `Blizzard_ArrowCalloutFrame/ArrowCalloutFrame.lua` |
| ✅ | `HIDE_HYPERLINK_TOOLTIP` |  |  | [TooltipInfo](systems/TooltipInfo.md) |
| ✅ | `HIDE_SUBTITLE` |  |  | [Cinematic](systems/Cinematic.md) |
| ✅ | `HONOR_LEVEL_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `HONOR_XP_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `HOUSE_DECOR_ADDED_TO_CHEST` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSE_EDITOR_AVAILABILITY_CHANGED` |  |  | [HouseEditorUI](systems/HouseEditorUI.md) |
| ✅ | `HOUSE_EDITOR_MODE_CHANGED` |  |  | [HouseEditorUI](systems/HouseEditorUI.md) |
| ✅ | `HOUSE_EDITOR_MODE_CHANGE_FAILURE` |  |  | [HouseEditorUI](systems/HouseEditorUI.md) |
| ✅ | `HOUSE_EXTERIOR_DECOR_HIDDEN_CHANGED` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSE_EXTERIOR_POSITION_FAILURE` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSE_EXTERIOR_POSITION_SUCCESS` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSE_EXTERIOR_TYPE_UNLOCKED` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSE_FINDER_NEIGHBORHOOD_DATA_RECIEVED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSE_INFO_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSE_LEVEL_CHANGED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSE_LEVEL_FAVOR_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSE_PLOT_ENTERED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSE_PLOT_EXITED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSE_RESERVATION_RESPONSE_RECIEVED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSE_RESET_COMPLETED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSE_RESET_FAILED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSING_BASIC_MODE_HOVERED_TARGET_CHANGED` |  |  | [HousingBasicModeUI](systems/HousingBasicModeUI.md) |
| ✅ | `HOUSING_BASIC_MODE_PLACEMENT_FLAGS_UPDATED` |  |  | [HousingBasicModeUI](systems/HousingBasicModeUI.md) |
| ✅ | `HOUSING_BASIC_MODE_SELECTED_TARGET_CHANGED` |  |  | [HousingBasicModeUI](systems/HousingBasicModeUI.md) |
| ✅ | `HOUSING_BLUEPRINTS_AVAILABILITY_CHANGED` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_COLLECTION_FAILURE` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_COLLECTION_RECEIVED` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_CONTENTS_FAILURE` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_CONTENTS_RECEIVED` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_DELETE_FAILURE` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_DELETE_SUCCESS` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_EXPORT_FAILURE` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_EXPORT_SUCCESS` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_IMPORT_FAILURE` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_IMPORT_STARTED` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_IMPORT_SUCCESS` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_RENAME_FAILURE` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_BLUEPRINT_RENAME_SUCCESS` |  |  | [HousingBlueprintUI](systems/HousingBlueprintUI.md) |
| ✅ | `HOUSING_CATALOG_CATEGORY_UPDATED` |  |  | [HousingCatalogUI](systems/HousingCatalogUI.md) |
| ✅ | `HOUSING_CATALOG_SUBCATEGORY_UPDATED` |  |  | [HousingCatalogUI](systems/HousingCatalogUI.md) |
| ✅ | `HOUSING_CLEANUP_MODE_HOVERED_TARGET_CHANGED` |  |  | [HousingCleanupModeUI](systems/HousingCleanupModeUI.md) |
| ✅ | `HOUSING_CLEANUP_MODE_TARGET_SELECTED` |  |  | [HousingCleanupModeUI](systems/HousingCleanupModeUI.md) |
| ✅ | `HOUSING_CORE_FIXTURE_CHANGED` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_CUSTOMIZE_MODE_HOVERED_TARGET_CHANGED` |  |  | [HousingCustomizeModeUI](systems/HousingCustomizeModeUI.md) |
| ✅ | `HOUSING_CUSTOMIZE_MODE_SELECTED_TARGET_CHANGED` |  |  | [HousingCustomizeModeUI](systems/HousingCustomizeModeUI.md) |
| ✅ | `HOUSING_DECOR_ADD_TO_PREVIEW_LIST` |  |  | [HousingCatalogUI](systems/HousingCatalogUI.md) |
| ✅ | `HOUSING_DECOR_CUSTOMIZATION_CHANGED` |  |  | [HousingCustomizeModeUI](systems/HousingCustomizeModeUI.md) |
| ✅ | `HOUSING_DECOR_DYE_FAILURE` |  |  | [HousingCustomizeModeUI](systems/HousingCustomizeModeUI.md) |
| ✅ | `HOUSING_DECOR_FREE_PLACE_STATUS_CHANGED` |  |  | [HousingBasicModeUI](systems/HousingBasicModeUI.md) |
| ✅ | `HOUSING_DECOR_GRID_SNAP_OCCURRED` |  |  | [HousingBasicModeUI](systems/HousingBasicModeUI.md) |
| ✅ | `HOUSING_DECOR_GRID_SNAP_STATUS_CHANGED` |  |  | [HousingBasicModeUI](systems/HousingBasicModeUI.md) |
| ✅ | `HOUSING_DECOR_GRID_VISIBILITY_STATUS_CHANGED` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSING_DECOR_PLACE_FAILURE` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSING_DECOR_PLACE_SUCCESS` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSING_DECOR_PRECISION_MANIPULATION_EVENT` |  |  | [HousingExpertModeUI](systems/HousingExpertModeUI.md) |
| ✅ | `HOUSING_DECOR_PRECISION_MANIPULATION_STATUS_CHANGED` |  |  | [HousingExpertModeUI](systems/HousingExpertModeUI.md) |
| ✅ | `HOUSING_DECOR_PRECISION_SUBMODE_CHANGED` |  |  | [HousingExpertModeUI](systems/HousingExpertModeUI.md) |
| ✅ | `HOUSING_DECOR_PREVIEW_LIST_REMOVE_FROM_WORLD` |  |  | [HousingCatalogUI](systems/HousingCatalogUI.md) |
| ✅ | `HOUSING_DECOR_PREVIEW_LIST_UPDATED` |  |  | [HousingCatalogUI](systems/HousingCatalogUI.md) |
| ✅ | `HOUSING_DECOR_PREVIEW_STATE_CHANGED` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSING_DECOR_REMOVED` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSING_DECOR_SELECT_RESPONSE` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSING_EXPERT_MODE_HOVERED_TARGET_CHANGED` |  |  | [HousingExpertModeUI](systems/HousingExpertModeUI.md) |
| ✅ | `HOUSING_EXPERT_MODE_PLACEMENT_FLAGS_UPDATED` |  |  | [HousingExpertModeUI](systems/HousingExpertModeUI.md) |
| ✅ | `HOUSING_EXPERT_MODE_SELECTED_TARGET_CHANGED` |  |  | [HousingExpertModeUI](systems/HousingExpertModeUI.md) |
| ✅ | `HOUSING_FIXTURE_HOVER_CHANGED` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_FIXTURE_POINT_FRAMES_RELEASED` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_FIXTURE_POINT_FRAME_ADDED` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_FIXTURE_POINT_FRAME_RELEASED` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_FIXTURE_POINT_SELECTION_CHANGED` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_FIXTURE_UNLOCKED` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_INSPECT_MODE_DECOR_HOVERED_CHANGED` |  |  | [HousingInspectModeUI](systems/HousingInspectModeUI.md) |
| ✅ | `HOUSING_INSPECT_MODE_STATE_UPDATED` |  |  | [HousingInspectModeUI](systems/HousingInspectModeUI.md) |
| ✅ | `HOUSING_LAYOUT_DOOR_SELECTED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_DOOR_SELECTION_CHANGED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_DRAG_TARGET_CHANGED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_FLOORPLAN_SELECTION_CHANGED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_OCCUPIED_FLOOR_RANGE_CHANGED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_PIN_FRAMES_RELEASED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_PIN_FRAME_ADDED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_PIN_FRAME_RELEASED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_ROOM_COMPONENT_THEME_SET_CHANGED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_ROOM_MOVED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_ROOM_MOVE_INVALID` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_ROOM_RECEIVED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_ROOM_REMOVED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_ROOM_RETURNED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_ROOM_SELECTION_CHANGED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_ROOM_SNAPPED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_LAYOUT_VIEWED_FLOOR_CHANGED` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `HOUSING_MARKET_AVAILABILITY_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSING_NEW_DECOR_PLACE_COMPLETE` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSING_NUM_DECOR_PLACED_CHANGED` |  |  | [HousingDecorUI](systems/HousingDecorUI.md) |
| ✅ | `HOUSING_REFUND_LIST_UPDATED` |  |  | [HousingCatalogUI](systems/HousingCatalogUI.md) |
| ✅ | `HOUSING_ROOM_COMPONENT_CUSTOMIZATION_CHANGED` |  |  | [HousingCustomizeModeUI](systems/HousingCustomizeModeUI.md) |
| ✅ | `HOUSING_ROOM_COMPONENT_CUSTOMIZATION_CHANGE_FAILED` |  |  | [HousingCustomizeModeUI](systems/HousingCustomizeModeUI.md) |
| ✅ | `HOUSING_SERVICES_AVAILABILITY_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `HOUSING_SET_EXTERIOR_HOUSE_SIZE_RESPONSE` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_SET_EXTERIOR_HOUSE_TYPE_RESPONSE` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_SET_FIXTURE_RESPONSE` |  |  | [HouseExteriorUI](systems/HouseExteriorUI.md) |
| ✅ | `HOUSING_STORAGE_ENTRY_UPDATED` |  |  | [HousingCatalogUI](systems/HousingCatalogUI.md) |
| ✅ | `HOUSING_STORAGE_UPDATED` |  |  | [HousingCatalogUI](systems/HousingCatalogUI.md) |
| ⛔ | `HUNTER` |  |  | used in `Blizzard_FrameXMLBase/Camelot/Constants.lua` |
| ✅ | `IGNORELIST_UPDATE` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `IGNORE_NEIGHBORHOOD_RESPONSE` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `IMMERSIVE_INTERACTION_BEGIN` |  |  | [ImmersiveInteraction](systems/ImmersiveInteraction.md) |
| ✅ | `IMMERSIVE_INTERACTION_END` |  |  | [ImmersiveInteraction](systems/ImmersiveInteraction.md) |
| ⛔ | `INCOMING` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `INCOMING_RESURRECT_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `INCOMING_SUMMON_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `INITIAL_CLUBS_LOADED` | 1 | `` | [Club](systems/Club.md) |
| ✅ | `INITIAL_HOTFIXES_APPLIED` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `INITIATIVE_ACTIVITY_LOG_UPDATED` |  |  | [NeighborhoodInitiative](systems/NeighborhoodInitiative.md) |
| ✅ | `INITIATIVE_COMPLETED` |  |  | [NeighborhoodInitiative](systems/NeighborhoodInitiative.md) |
| ✅ | `INITIATIVE_TASKS_TRACKED_LIST_CHANGED` |  |  | [NeighborhoodInitiative](systems/NeighborhoodInitiative.md) |
| ✅ | `INITIATIVE_TASKS_TRACKED_UPDATED` |  |  | [NeighborhoodInitiative](systems/NeighborhoodInitiative.md) |
| ✅ | `INITIATIVE_TASK_COMPLETED` |  |  | [NeighborhoodInitiative](systems/NeighborhoodInitiative.md) |
| ✅ | `INPUT_DEVICE_INTERFACE_TRANSITION` |  |  | [Input](systems/Input.md) |
| ✅ | `INSPECT_ACHIEVEMENT_READY` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `INSPECT_HONOR_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `INSPECT_READY` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `INSTANCE_ABANDON_VOTE_FINISHED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `INSTANCE_ABANDON_VOTE_STARTED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `INSTANCE_ABANDON_VOTE_UPDATED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `INSTANCE_BOOT_START` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `INSTANCE_BOOT_STOP` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ⛔ | `INSTANCE_CHAT` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ⛔ | `INSTANCE_CHAT_LEADER` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `INSTANCE_ENCOUNTER_ADD_TIMER` |  |  | [InstanceEncounter](systems/InstanceEncounter.md) |
| ✅ | `INSTANCE_ENCOUNTER_ENGAGE_UNIT` |  |  | [InstanceEncounter](systems/InstanceEncounter.md) |
| ✅ | `INSTANCE_ENCOUNTER_OBJECTIVE_COMPLETE` |  |  | [InstanceEncounter](systems/InstanceEncounter.md) |
| ✅ | `INSTANCE_ENCOUNTER_OBJECTIVE_START` |  |  | [InstanceEncounter](systems/InstanceEncounter.md) |
| ✅ | `INSTANCE_ENCOUNTER_OBJECTIVE_UPDATE` |  |  | [InstanceEncounter](systems/InstanceEncounter.md) |
| ✅ | `INSTANCE_GROUP_SIZE_CHANGED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `INSTANCE_LEAVER_STATUS_CHANGED` |  |  | [InstanceLeaverInfo](systems/InstanceLeaverInfo.md) |
| ✅ | `INSTANCE_LOCK_START` |  |  | [EncounterInfo](systems/EncounterInfo.md) |
| ✅ | `INSTANCE_LOCK_STOP` | 1 | `` | [EncounterInfo](systems/EncounterInfo.md) |
| ✅ | `INSTANCE_LOCK_WARNING` |  |  | [EncounterInfo](systems/EncounterInfo.md) |
| ✅ | `INSTANCE_RESET_WARNING` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `INVENTORY_SEARCH_UPDATE` |  |  | [Container](systems/Container.md) |
| ⛔ | `INVITE_COMMUNITY_MEMBER` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ⛔ | `INVITE_COMMUNITY_MEMBER_WITH_INVITE_LINK` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ✅ | `INVITE_TO_PARTY_CONFIRMATION` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `INVITE_TRAVEL_PASS_CONFIRMATION` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `ISLANDS_QUEUE_CLOSE` |  |  | [IslandsQueue](systems/IslandsQueue.md) |
| ✅ | `ISLANDS_QUEUE_OPEN` |  |  | [IslandsQueue](systems/IslandsQueue.md) |
| ✅ | `ISLAND_AZERITE_GAIN` |  |  | [IslandsInfo](systems/IslandsInfo.md) |
| ✅ | `ISLAND_COMPLETED` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `ITEM_CHANGED` |  |  | [Item](systems/Item.md) |
| ✅ | `ITEM_CONVERSION_DATA_READY` |  |  | [Item](systems/Item.md) |
| ✅ | `ITEM_COUNT_CHANGED` | 2 | `n` | [Item](systems/Item.md) |
| ✅ | `ITEM_DATA_LOAD_RESULT` | 3 | `n,b` | [Item](systems/Item.md) |
| ✅ | `ITEM_INTERACTION_CHARGE_INFO_UPDATED` |  |  | [ItemInteractionUI](systems/ItemInteractionUI.md) |
| ✅ | `ITEM_INTERACTION_ITEM_SELECTION_UPDATED` |  |  | [ItemInteractionUI](systems/ItemInteractionUI.md) |
| ✅ | `ITEM_KEY_ITEM_INFO_RECEIVED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `ITEM_LOCKED` |  |  | [Container](systems/Container.md) |
| ✅ | `ITEM_LOCK_CHANGED` |  |  | [Container](systems/Container.md) |
| ✅ | `ITEM_PURCHASED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `ITEM_PUSH` | 2 | `n,n` | [Loot](systems/Loot.md) |
| ✅ | `ITEM_RESTORATION_BUTTON_STATUS` |  |  | [GMTicketInfo](systems/GMTicketInfo.md) |
| ✅ | `ITEM_SEARCH_RESULTS_ADDED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `ITEM_SEARCH_RESULTS_UPDATED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `ITEM_TEXT_BEGIN` |  |  | [ItemText](systems/ItemText.md) |
| ✅ | `ITEM_TEXT_CLOSED` |  |  | [ItemText](systems/ItemText.md) |
| ✅ | `ITEM_TEXT_READY` |  |  | [ItemText](systems/ItemText.md) |
| ✅ | `ITEM_TEXT_TRANSLATION` |  |  | [ItemText](systems/ItemText.md) |
| ✅ | `ITEM_UNLOCKED` |  |  | [Container](systems/Container.md) |
| ✅ | `ITEM_UPGRADE_FAILED` |  |  | [ItemUpgrade](systems/ItemUpgrade.md) |
| ✅ | `ITEM_UPGRADE_MASTER_SET_ITEM` |  |  | [ItemUpgrade](systems/ItemUpgrade.md) |
| ✅ | `ITEM_UPGRADE_MASTER_UPDATE` |  |  | [ItemUpgrade](systems/ItemUpgrade.md) |
| ✅ | `JAILERS_TOWER_LEVEL_UPDATE` |  |  | [ScenarioInfo](systems/ScenarioInfo.md) |
| 🆕 | `KEY_BINDINGS_COPY_COMPLETE` |  |  | used in `Blizzard_GlueXML/Camelot/CharacterCopy.lua` |
| 🆕 | `KIOSK_ENABLED` |  |  | used in `Blizzard_GlueParent/Mainline/GlueParent.lua` |
| 🆕 | `KIOSK_HOUSING_RESET` |  |  | used in `Blizzard_Kiosk/Gamescom2025/Game.lua` |
| 🆕 | `KIOSK_SESSION_EXPIRATION_CHANGED` |  |  | used in `Blizzard_Kiosk/Kiosk.lua` |
| 🆕 | `KIOSK_SESSION_EXPIRATION_WARNING` |  |  | used in `Blizzard_Kiosk/Kiosk.lua` |
| 🆕 | `KIOSK_SESSION_EXPIRED` |  |  | used in `Blizzard_GamepadSmartNavigation/SmartNavigation.lua` |
| 🆕 | `KIOSK_SESSION_RESTART` |  |  | used in `Blizzard_Kiosk/Kiosk.lua` |
| 🆕 | `KIOSK_SESSION_SHUTDOWN` |  |  | used in `Blizzard_Kiosk/Kiosk.lua` |
| 🆕 | `KIOSK_SESSION_STARTED` |  |  | used in `Blizzard_Kiosk/Kiosk.lua` |
| ⛔ | `KNEEL` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `KNOWN_TITLES_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `LANGUAGE_LIST_CHANGED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ⛔ | `LAUGH` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| 🆕 | `LAUNCHER_LOGIN_STATUS_CHANGED` |  |  | used in `Blizzard_GlueXML/Mainline/AccountLogin.lua` |
| ✅ | `LEARNED_SPELL_IN_SKILL_LINE` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `LEAVE_PARTY_CONFIRMATION` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `LEAVING_TUTORIAL_AREA` |  |  | [Tutorial](systems/Tutorial.md) |
| ✅ | `LEGACY_FRIEND_SYSTEM_STATUS_UPDATED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `LEGACY_LOOT_RULES_CHANGED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `LET_RECENT_ALLIES_SEE_LOCATION_SETTING_UPDATED` |  |  | [RecentAllies](systems/RecentAllies.md) |
| ⛔ | `LEVEL_TOO_HIGH` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ⛔ | `LEVEL_TOO_LOW` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ✅ | `LFG_BOOT_PROPOSAL_UPDATE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_COMPLETION_REWARD` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_COOLDOWNS_UPDATED` | 1 | `` | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_ENABLED_STATE_CHANGED` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_GROUP_DELISTED_LEADERSHIP_CHANGE` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_INVALID_ERROR_MESSAGE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_LIST_ACTIVE_ENTRY_UPDATE` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_APPLICANT_LIST_UPDATED` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_APPLICANT_UPDATED` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_APPLICATION_STATUS_UPDATED` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_AVAILABILITY_UPDATE` | 1 | `` | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_CENSORED_ACTIVE_ENTRY_UPDATE` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_ENTRY_CREATION_FAILED` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_ENTRY_EXPIRED_TIMEOUT` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_ENTRY_EXPIRED_TOO_MANY_PLAYERS` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_JOINED_GROUP` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_REVEALED_CENSORED_ACTIVE_ENTRY` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_ROLE_UPDATE` |  |  | [LFGListRoles](systems/LFGListRoles.md) |
| ✅ | `LFG_LIST_SEARCH_FAILED` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_SEARCH_RESULTS_RECEIVED` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_SEARCH_RESULT_UPDATED` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_SHOW_SEARCH` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LIST_UPDATE_SEARCH_RESULTS` |  |  | [LFGList](systems/LFGList.md) |
| ✅ | `LFG_LOCK_INFO_RECEIVED` | 1 | `` | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_OFFER_CONTINUE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_OPEN_FROM_GOSSIP` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_PROPOSAL_DONE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_PROPOSAL_FAILED` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_PROPOSAL_SHOW` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_PROPOSAL_SUCCEEDED` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_PROPOSAL_UPDATE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_QUEUE_STATUS_UPDATE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_READY_CHECK_DECLINED` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_READY_CHECK_HIDE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_READY_CHECK_PLAYER_IS_READY` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_READY_CHECK_SHOW` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_READY_CHECK_UPDATE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_ROLE_CHECK_DECLINED` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_ROLE_CHECK_HIDE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_ROLE_CHECK_ROLE_CHOSEN` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_ROLE_CHECK_SHOW` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_ROLE_CHECK_UPDATE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_ROLE_UPDATE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_UPDATE` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LFG_UPDATE_RANDOM_INFO` | 1 | `` | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `LIFESTEAL_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `LOADING_SCREEN_DISABLED` | 1 | `` | [LoadingScreen](systems/LoadingScreen.md) |
| ✅ | `LOADING_SCREEN_ENABLED` | 1 | `` | [LoadingScreen](systems/LoadingScreen.md) |
| 🆕 | `LOBBY_MATCHMAKER_PARTY_UPDATE` |  |  | used in `Blizzard_GlueXML/WoWLabs/GluePartyPoseUI.lua` |
| ✅ | `LOBBY_MATCHMAKER_QUEUE_ABANDONED` |  |  | [LobbyMatchmakerInfo](systems/LobbyMatchmakerInfo.md) |
| ✅ | `LOBBY_MATCHMAKER_QUEUE_ERROR` |  |  | [LobbyMatchmakerInfo](systems/LobbyMatchmakerInfo.md) |
| ✅ | `LOBBY_MATCHMAKER_QUEUE_EXPIRED` |  |  | [LobbyMatchmakerInfo](systems/LobbyMatchmakerInfo.md) |
| ✅ | `LOBBY_MATCHMAKER_QUEUE_POPPED` |  |  | [LobbyMatchmakerInfo](systems/LobbyMatchmakerInfo.md) |
| ✅ | `LOBBY_MATCHMAKER_QUEUE_STATUS_UPDATE` |  |  | [LobbyMatchmakerInfo](systems/LobbyMatchmakerInfo.md) |
| ✅ | `LOCALPLAYER_PET_RENAMED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `LOC_RESULT` |  |  | [SystemInfo](systems/SystemInfo.md) |
| 🆕 | `LOGIN_STATE_CHANGED` |  |  | used in `Blizzard_GlueParent/Mainline/GlueParent.lua` |
| ✅ | `LOGOUT_CANCEL` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `LOOT_BIND_CONFIRM` |  |  | [Loot](systems/Loot.md) |
| ✅ | `LOOT_CLOSED` | 4 | `` | [Loot](systems/Loot.md) |
| ✅ | `LOOT_HISTORY_CLEAR_HISTORY` |  |  | [LootHistory](systems/LootHistory.md) |
| ✅ | `LOOT_HISTORY_GO_TO_ENCOUNTER` |  |  | [LootHistory](systems/LootHistory.md) |
| ✅ | `LOOT_HISTORY_ONE_HUNDRED_ROLL` |  |  | [LootHistory](systems/LootHistory.md) |
| ✅ | `LOOT_HISTORY_UPDATE_DROP` |  |  | [LootHistory](systems/LootHistory.md) |
| ✅ | `LOOT_HISTORY_UPDATE_ENCOUNTER` |  |  | [LootHistory](systems/LootHistory.md) |
| ✅ | `LOOT_ITEM_AVAILABLE` |  |  | [Loot](systems/Loot.md) |
| ✅ | `LOOT_ITEM_ROLL_WON` |  |  | [Loot](systems/Loot.md) |
| ✅ | `LOOT_JOURNAL_ITEM_UPDATE` |  |  | [LootJournal](systems/LootJournal.md) |
| ✅ | `LOOT_OPENED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `LOOT_READY` | 2 | `b` | [Loot](systems/Loot.md) |
| ✅ | `LOOT_ROLLS_COMPLETE` |  |  | [Loot](systems/Loot.md) |
| ✅ | `LOOT_SLOT_CHANGED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `LOOT_SLOT_CLEARED` | 2 | `n` | [Loot](systems/Loot.md) |
| ✅ | `LORE_TEXT_UPDATED_CAMPAIGN` |  |  | [LoreText](systems/LoreText.md) |
| ✅ | `LOSS_OF_CONTROL_ADDED` |  |  | [LossOfControl](systems/LossOfControl.md) |
| ✅ | `LOSS_OF_CONTROL_COMMENTATOR_ADDED` |  |  | [LossOfControl](systems/LossOfControl.md) |
| ✅ | `LOSS_OF_CONTROL_COMMENTATOR_UPDATE` |  |  | [LossOfControl](systems/LossOfControl.md) |
| ✅ | `LOSS_OF_CONTROL_UPDATE` |  |  | [LossOfControl](systems/LossOfControl.md) |
| ✅ | `LUA_WARNING` | 3 | `s` | [ScriptWarnings](systems/ScriptWarnings.md) |
| ✅ | `MACRO_ACTION_BLOCKED` |  |  | [RestrictedActions](systems/RestrictedActions.md) |
| ✅ | `MACRO_ACTION_FORBIDDEN` |  |  | [RestrictedActions](systems/RestrictedActions.md) |
| ✅ | `MAIL_CLOSED` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIL_FAILED` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIL_INBOX_UPDATE` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIL_LOCK_SEND_ITEMS` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIL_OPEN_ALL_CANCELED` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIL_SEND_INFO_UPDATE` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIL_SEND_SUCCESS` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIL_SHOW` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIL_SUCCESS` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIL_UNLOCK_SEND_ITEMS` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `MAIN_SPEC_NEED_ROLL` |  |  | [Loot](systems/Loot.md) |
| ✅ | `MAJOR_FACTION_INTERACTION_ENDED` |  |  | [MajorFactionsUI](systems/MajorFactionsUI.md) |
| ✅ | `MAJOR_FACTION_INTERACTION_STARTED` |  |  | [MajorFactionsUI](systems/MajorFactionsUI.md) |
| ✅ | `MAJOR_FACTION_RENOWN_LEVEL_CHANGED` |  |  | [MajorFactionsUI](systems/MajorFactionsUI.md) |
| ✅ | `MAJOR_FACTION_UNLOCKED` |  |  | [MajorFactionsUI](systems/MajorFactionsUI.md) |
| ✅ | `MAP_EXPLORATION_UPDATED` |  |  | [MapExplorationInfo](systems/MapExplorationInfo.md) |
| 🆕 | `MAP_SCENE_CHARACTER_ON_MOUSE_ENTER` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectUI.lua` |
| 🆕 | `MAP_SCENE_CHARACTER_ON_MOUSE_LEAVE` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectUI.lua` |
| 🆕 | `MAP_SCENE_CHARACTER_UPDATE_OVERLAY_FRAME` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectUI.lua` |
| ✅ | `MASTERY_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `MAX_EXPANSION_LEVEL_UPDATED` |  |  | [Expansion](systems/Expansion.md) |
| ✅ | `MAX_SPELL_START_RECOVERY_OFFSET_CHANGED` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `MENTORSHIP_STATUS_CHANGED` | 1 | `` | [PlayerMentorship](systems/PlayerMentorship.md) |
| ✅ | `MERCHANT_CLOSED` |  |  | [MerchantFrame](systems/MerchantFrame.md) |
| ✅ | `MERCHANT_CONFIRM_TRADE_TIMER_REMOVAL` |  |  | [Item](systems/Item.md) |
| ✅ | `MERCHANT_FILTER_ITEM_UPDATE` |  |  | [MerchantFrame](systems/MerchantFrame.md) |
| ✅ | `MERCHANT_SHOW` |  |  | [MerchantFrame](systems/MerchantFrame.md) |
| ✅ | `MERCHANT_UPDATE` |  |  | [MerchantFrame](systems/MerchantFrame.md) |
| ⛔ | `MINIMAP_PING` |  |  | [Minimap](systems/Minimap.md) |
| ✅ | `MINIMAP_UPDATE_TRACKING` |  |  | [Minimap](systems/Minimap.md) |
| ✅ | `MINIMAP_UPDATE_ZOOM` | 1 | `` | [Minimap](systems/Minimap.md) |
| ✅ | `MIN_EXPANSION_LEVEL_UPDATED` |  |  | [Expansion](systems/Expansion.md) |
| ✅ | `MIRROR_TIMER_PAUSE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `MIRROR_TIMER_START` |  |  | [Unit](systems/Unit.md) |
| ✅ | `MIRROR_TIMER_STOP` |  |  | [Unit](systems/Unit.md) |
| ✅ | `MODIFIER_STATE_CHANGED` | 6 | `s,n` | [KeyBindings](systems/KeyBindings.md) |
| ⛔ | `MONEY` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ⛔ | `MONSTER_EMOTE` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ⛔ | `MONSTER_SAY` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ⛔ | `MONSTER_WHISPER` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ⛔ | `MONSTER_YELL` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `MOUNT_CURSOR_CLEAR` |  |  | [Cursor](systems/Cursor.md) |
| ✅ | `MOUNT_EQUIPMENT_APPLY_RESULT` |  |  | [MountJournal](systems/MountJournal.md) |
| ✅ | `MOUNT_JOURNAL_SEARCH_UPDATED` | 1 | `` | [MountJournal](systems/MountJournal.md) |
| ✅ | `MOUNT_JOURNAL_USABILITY_CHANGED` | 1 | `` | [MountJournal](systems/MountJournal.md) |
| ⛔ | `MOVEBACKWARD` |  |  | used in `Blizzard_BoostTutorial/Blizzard_TutorialKeyboardMouseFrame.lua` |
| ⛔ | `MOVEFORWARD` |  |  | used in `Blizzard_BoostTutorial/Blizzard_TutorialKeyboardMouseFrame.lua` |
| ✅ | `MOVE_OUT_RESERVATION_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `MUTELIST_UPDATE` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `MYTHIC_PLUS_CURRENT_AFFIX_UPDATE` |  |  | [MythicPlusInfo](systems/MythicPlusInfo.md) |
| ✅ | `MYTHIC_PLUS_NEW_WEEKLY_RECORD` |  |  | [MythicPlusInfo](systems/MythicPlusInfo.md) |
| ✅ | `NAME_PLATE_CREATED` | 1 | `t` | [NamePlateManager](systems/NamePlateManager.md) |
| ✅ | `NAME_PLATE_UNIT_ADDED` | 4 | `s` | [NamePlateManager](systems/NamePlateManager.md) |
| ✅ | `NAME_PLATE_UNIT_BEHIND_CAMERA_CHANGED` |  |  | [NamePlateManager](systems/NamePlateManager.md) |
| ✅ | `NAME_PLATE_UNIT_REMOVED` | 4 | `s` | [NamePlateManager](systems/NamePlateManager.md) |
| ✅ | `NAVIGATION_DESTINATION_REACHED` |  |  | [InGameNavigation](systems/InGameNavigation.md) |
| ✅ | `NAVIGATION_FRAME_CREATED` | 1 | `t` | [InGameNavigation](systems/InGameNavigation.md) |
| ✅ | `NAVIGATION_FRAME_DESTROYED` | 1 | `` | [InGameNavigation](systems/InGameNavigation.md) |
| ✅ | `NEIGHBORHOOD_GUILD_SIZE_VALIDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `NEIGHBORHOOD_INFO_UPDATED` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `NEIGHBORHOOD_INITIATIVE_UPDATED` |  |  | [NeighborhoodInitiative](systems/NeighborhoodInitiative.md) |
| ✅ | `NEIGHBORHOOD_INVITE_RESPONSE` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `NEIGHBORHOOD_LIST_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `NEIGHBORHOOD_MAP_DATA_UPDATED` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `NEIGHBORHOOD_NAME_UPDATED` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `NEIGHBORHOOD_NAME_VALIDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `NEUTRAL_FACTION_SELECT_RESULT` |  |  | [Unit](systems/Unit.md) |
| ✅ | `NEWCOMER_GRADUATION` |  |  | [PlayerMentorship](systems/PlayerMentorship.md) |
| ✅ | `NEW_HOUSING_ITEM_ACQUIRED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `NEW_MATCHMAKING_PARTY_INVITE` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `NEW_MOUNT_ADDED` |  |  | [MountJournal](systems/MountJournal.md) |
| ✅ | `NEW_PET_ADDED` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `NEW_RECIPE_LEARNED` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `NEW_RUNEFORGE_POWER_ADDED` |  |  | [LegendaryCrafting](systems/LegendaryCrafting.md) |
| ✅ | `NEW_TOY_ADDED` |  |  | [ToyBoxInfo](systems/ToyBoxInfo.md) |
| ✅ | `NEW_WARBAND_SCENE_ADDED` |  |  | [WarbandSceneInfo](systems/WarbandSceneInfo.md) |
| ✅ | `NEW_WMO_CHUNK` |  |  | [MapUI](systems/MapUI.md) |
| ✅ | `NOTCHED_DISPLAY_MODE_CHANGED` |  |  | [UI](systems/UI.md) |
| ✅ | `NOTIFY_CHAT_SUPPRESSED` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `NOTIFY_PVP_AFK_RESULT` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `NOTIFY_TURN_STRAFE_CHANGE` |  |  | [KeyBindings](systems/KeyBindings.md) |
| ⛔ | `NO_SPEC` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ⛔ | `NO_VALID_ROLES` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ✅ | `NPE_TUTORIAL_UPDATE` |  |  | [Tutorial](systems/Tutorial.md) |
| ✅ | `OBJECT_ENTERED_AOI` |  |  | [Unit](systems/Unit.md) |
| ✅ | `OBJECT_LEFT_AOI` |  |  | [Unit](systems/Unit.md) |
| ✅ | `OBLITERUM_FORGE_PENDING_ITEM_CHANGED` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ⛔ | `OFFICER` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ⛔ | `OPENFIRE` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `OPEN_CHARTER_CONFIRMATION_UI` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `OPEN_CREATE_CHARTER_NEIGHBORHOOD_UI` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `OPEN_CREATE_GUILD_NEIGHBORHOOD_UI` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `OPEN_MASTER_LOOT_LIST` |  |  | [Loot](systems/Loot.md) |
| ✅ | `OPEN_NEIGHBORHOOD_CHARTER` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `OPEN_NEIGHBORHOOD_CHARTER_SIGNATURE_REQUEST` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `OPEN_PLOT_CORNERSTONE` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `OPEN_RECIPE_RESPONSE` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `OPEN_SPLASH_SCREEN` | 1 | `-` | [SplashScreen](systems/SplashScreen.md) |
| 🆕 | `OPEN_STATUS_DIALOG` |  |  | used in `Blizzard_GlueParent/Mainline/GlueParent.lua` |
| ✅ | `OPEN_TABARD_FRAME` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `OWNED_AUCTIONS_UPDATED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `OWNED_AUCTION_BIDDER_INFO_RECEIVED` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ⛔ | `PALADIN` |  |  | used in `Blizzard_FrameXMLBase/Camelot/Constants.lua` |
| ⛔ | `PARTY` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `PARTY_ELIGIBILITY_FOR_DELVE_TIERS_CHANGED` |  |  | [DelvesUI](systems/DelvesUI.md) |
| ✅ | `PARTY_INVITE_CANCEL` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `PARTY_INVITE_REQUEST` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `PARTY_KILL` | 1 | `s,s` | [Unit](systems/Unit.md) |
| ⛔ | `PARTY_LEADER` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `PARTY_LEADER_CHANGED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `PARTY_LFG_RESTRICTED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `PARTY_LOOT_METHOD_CHANGED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `PARTY_MEMBER_DISABLE` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `PARTY_MEMBER_ENABLE` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `PENDING_AZERITE_ESSENCE_CHANGED` |  |  | [AzeriteEssence](systems/AzeriteEssence.md) |
| ✅ | `PENDING_NEIGHBORHOOD_INVITES_RECIEVED` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `PERKS_ACTIVITIES_TRACKED_LIST_CHANGED` |  |  | [PerksActivities](systems/PerksActivities.md) |
| ✅ | `PERKS_ACTIVITIES_TRACKED_UPDATED` |  |  | [PerksActivities](systems/PerksActivities.md) |
| ✅ | `PERKS_ACTIVITIES_UPDATED` |  |  | [PerksActivities](systems/PerksActivities.md) |
| ✅ | `PERKS_ACTIVITY_COMPLETED` |  |  | [PerksActivities](systems/PerksActivities.md) |
| ✅ | `PERKS_PROGRAM_ADD_PENDING_SHOP_ITEM` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_CLOSE` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_CURRENCY_AWARDED` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_CURRENCY_REFRESH` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_DATA_REFRESH` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_DATA_SPECIFIC_ITEM_REFRESH` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_DISABLED` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_OPEN` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_PURCHASE_CART_SUCCESS` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_PURCHASE_SUCCESS` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_REFUND_SUCCESS` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_REMOVE_PENDING_SHOP_ITEM` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_RESULT_ERROR` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PERKS_PROGRAM_SET_FROZEN_ITEM` |  |  | [PerksProgram](systems/PerksProgram.md) |
| ✅ | `PETITION_CLOSED` |  |  | [GMTicketInfo](systems/GMTicketInfo.md) |
| ✅ | `PETITION_SHOW` |  |  | [GMTicketInfo](systems/GMTicketInfo.md) |
| ✅ | `PET_ATTACK_START` |  |  | [PetInfo](systems/PetInfo.md) |
| ✅ | `PET_ATTACK_STOP` |  |  | [PetInfo](systems/PetInfo.md) |
| ✅ | `PET_BAR_HIDEGRID` |  |  | [PetInfo](systems/PetInfo.md) |
| ✅ | `PET_BAR_SHOWGRID` |  |  | [PetInfo](systems/PetInfo.md) |
| ✅ | `PET_BAR_UPDATE` |  |  | [ActionBar](systems/ActionBar.md) |
| ✅ | `PET_BAR_UPDATE_COOLDOWN` |  |  | [PetInfo](systems/PetInfo.md) |
| ✅ | `PET_BAR_UPDATE_USABLE` | 9 | `` | [Unit](systems/Unit.md) |
| ✅ | `PET_BATTLE_ABILITY_CHANGED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_ACTION_SELECTED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_AURA_APPLIED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_AURA_CANCELED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_AURA_CHANGED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_CAPTURED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_CLOSE` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_FINAL_ROUND` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_HEALTH_CHANGED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_LEVEL_CHANGED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_LOOT_RECEIVED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `PET_BATTLE_MAX_HEALTH_CHANGED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_OPENING_DONE` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_OPENING_START` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_OVER` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_OVERRIDE_ABILITY` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_PET_CHANGED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_PET_ROUND_PLAYBACK_COMPLETE` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_PET_ROUND_RESULTS` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_PET_TYPE_CHANGED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_PVP_DUEL_REQUESTED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_PVP_DUEL_REQUEST_CANCEL` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_QUEUE_PROPOSAL_ACCEPTED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_QUEUE_PROPOSAL_DECLINED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_QUEUE_PROPOSE_MATCH` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_QUEUE_STATUS` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_BATTLE_XP_CHANGED` |  |  | [BattlePet](systems/BattlePet.md) |
| ✅ | `PET_DISMISS_START` |  |  | [PetInfo](systems/PetInfo.md) |
| ✅ | `PET_FORCE_NAME_DECLENSION` |  |  | [PetInfo](systems/PetInfo.md) |
| ✅ | `PET_INFO_UPDATE` |  |  | [StableInfo](systems/StableInfo.md) |
| ✅ | `PET_JOURNAL_AUTO_SLOTTED_PET` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `PET_JOURNAL_CAGE_FAILED` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `PET_JOURNAL_LIST_UPDATE` | 2 | `` | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `PET_JOURNAL_NEW_BATTLE_SLOT` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `PET_JOURNAL_PETS_HEALED` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `PET_JOURNAL_PET_DELETED` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `PET_JOURNAL_PET_RESTORED` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `PET_JOURNAL_PET_REVOKED` |  |  | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `PET_JOURNAL_TRAP_LEVEL_SET` | 1 | `n` | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `PET_ORDER_MOVE_TO_PENDING_CHANGED` |  |  | [PetInfo](systems/PetInfo.md) |
| ✅ | `PET_SPECIALIZATION_CHANGED` |  |  | [SpecializationInfo](systems/SpecializationInfo.md) |
| ✅ | `PET_STABLE_CLOSED` |  |  | [StableInfo](systems/StableInfo.md) |
| ✅ | `PET_STABLE_FAVORITES_UPDATED` |  |  | [StableInfo](systems/StableInfo.md) |
| ✅ | `PET_STABLE_SHOW` |  |  | [StableInfo](systems/StableInfo.md) |
| ✅ | `PET_STABLE_UPDATE` |  |  | [StableInfo](systems/StableInfo.md) |
| ⛔ | `PET_STABLE_UPDATE_PAPERDOLL` |  |  | used in `Blizzard_UIPanels_Game/Cata/PetStable.lua` |
| ✅ | `PET_STATS_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `PET_UI_CLOSE` |  |  | [PetInfo](systems/PetInfo.md) |
| ✅ | `PET_UI_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PHOTO_SHARING_AUTHORIZATION_NEEDED` |  |  | [PhotoSharingUI](systems/PhotoSharingUI.md) |
| ✅ | `PHOTO_SHARING_AUTHORIZATION_UPDATED` |  |  | [PhotoSharingUI](systems/PhotoSharingUI.md) |
| ✅ | `PHOTO_SHARING_PHOTO_UPLOAD_STATUS` |  |  | [PhotoSharingUI](systems/PhotoSharingUI.md) |
| ✅ | `PHOTO_SHARING_SCREENSHOT_READY` |  |  | [PhotoSharingUI](systems/PhotoSharingUI.md) |
| ✅ | `PHOTO_SHARING_THIRD_PARTY_AUTHORIZATION_NEEDED` |  |  | [PhotoSharingUI](systems/PhotoSharingUI.md) |
| ✅ | `PING_SYSTEM_ERROR` |  |  | [PingManager](systems/PingManager.md) |
| ⛔ | `PLAYERBANKBAGSLOTS_CHANGED` |  |  | used in `Blizzard_UIPanels_Game/Vanilla/BankFrame.lua` |
| ✅ | `PLAYERBANKSLOTS_CHANGED` |  |  | [Bank](systems/Bank.md) |
| ✅ | `PLAYER_ACCOUNT_BANK_TAB_SLOTS_CHANGED` |  |  | [Bank](systems/Bank.md) |
| ✅ | `PLAYER_ALIVE` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `PLAYER_AVG_ITEM_LEVEL_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `PLAYER_CAMPING` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `PLAYER_CAN_GLIDE_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_CHARACTER_LIST_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `PLAYER_CHOICE_CLOSE` |  |  | [PlayerChoice](systems/PlayerChoice.md) |
| ✅ | `PLAYER_CHOICE_UPDATE` |  |  | [PlayerChoice](systems/PlayerChoice.md) |
| ✅ | `PLAYER_CONTROL_GAINED` |  |  | [LossOfControl](systems/LossOfControl.md) |
| ✅ | `PLAYER_CONTROL_LOST` |  |  | [LossOfControl](systems/LossOfControl.md) |
| ✅ | `PLAYER_DAMAGE_DONE_MODS` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_DEAD` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `PLAYER_DIFFICULTY_CHANGED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `PLAYER_ENTERING_BATTLEGROUND` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PLAYER_ENTERING_WORLD` | 1 | `b,b` | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `PLAYER_ENTER_COMBAT` | 1 | `` | [Unit](systems/Unit.md) |
| 🆕 | `PLAYER_EQUIPED_SPELLS_CHANGED` | 16 | `n` | used in `Blizzard_ActionBar/WoWLabs/ActionButtonOverrides.lua` |
| ✅ | `PLAYER_EQUIPMENT_CHANGED` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `PLAYER_FARSIGHT_FOCUS_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_FLAGS_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_FOCUS_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_GAINS_VEHICLE_DATA` |  |  | [Vehicle](systems/Vehicle.md) |
| ✅ | `PLAYER_GUILD_UPDATE` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `PLAYER_HOUSE_LIST_UPDATED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `PLAYER_IMPULSE_APPLIED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_INSIDE_QUEST_BLOB_STATE_CHANGED` | 6 | `n,b` | [Minimap](systems/Minimap.md) |
| ✅ | `PLAYER_INTERACTION_MANAGER_FRAME_HIDE` |  |  | [PlayerInteractionManager](systems/PlayerInteractionManager.md) |
| ✅ | `PLAYER_INTERACTION_MANAGER_FRAME_SHOW` |  |  | [PlayerInteractionManager](systems/PlayerInteractionManager.md) |
| ✅ | `PLAYER_IN_COMBAT_CHANGED` | 2 | `b` | [PlayerScript](systems/PlayerScript.md) |
| ✅ | `PLAYER_IS_GLIDING_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_JOINED_PVP_MATCH` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PLAYER_LEARN_PVP_TALENT_FAILED` |  |  | [SpecializationInfo](systems/SpecializationInfo.md) |
| ✅ | `PLAYER_LEARN_TALENT_FAILED` |  |  | [SpecializationInfo](systems/SpecializationInfo.md) |
| ✅ | `PLAYER_LEAVE_COMBAT` | 1 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_LEAVING_WORLD` | 1 | `` | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `PLAYER_LEVEL_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_LEVEL_UP` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_LOGIN` | 1 | `` | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `PLAYER_LOGOUT` | 1 | `` | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `PLAYER_LOOT_SPEC_UPDATED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `PLAYER_LOSES_VEHICLE_DATA` |  |  | [Vehicle](systems/Vehicle.md) |
| ✅ | `PLAYER_MAP_CHANGED` |  |  | [MapUI](systems/MapUI.md) |
| ✅ | `PLAYER_MAX_LEVEL_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_MONEY` |  |  | [CurrencySystem](systems/CurrencySystem.md) |
| ✅ | `PLAYER_MOUNT_DISPLAY_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_PVP_FLAG_CHANGED` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PLAYER_PVP_KILLS_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_PVP_RANK_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_PVP_TALENT_UPDATE` | 1 | `` | [SpecializationInfo](systems/SpecializationInfo.md) |
| ✅ | `PLAYER_QUITING` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `PLAYER_REGEN_DISABLED` | 1 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_REGEN_ENABLED` | 1 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_REPORT_SUBMITTED` |  |  | [GMTicketInfo](systems/GMTicketInfo.md) |
| ✅ | `PLAYER_ROLES_ASSIGNED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `PLAYER_SKINNED` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `PLAYER_SOFT_ENEMY_CHANGED` | 2 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_SOFT_FRIEND_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_SOFT_INTERACT_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_SOFT_TARGET_INTERACTION` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_SPECIALIZATION_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_STARTED_LOOKING` | 9 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_STARTED_MOVING` | 20 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_STARTED_TURNING` | 11 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_STOPPED_LOOKING` | 9 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_STOPPED_MOVING` | 20 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_STOPPED_TURNING` | 11 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_SWING` | 27 | `n,n` | [SwingTimer](systems/SwingTimer.md) |
| ✅ | `PLAYER_SWING_RANGE_UPDATE` |  |  | [SwingTimer](systems/SwingTimer.md) |
| ✅ | `PLAYER_TALENT_UPDATE` | 1 | `` | [SpecializationInfo](systems/SpecializationInfo.md) |
| ✅ | `PLAYER_TARGET_CHANGED` | 6 | `` | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_TARGET_DIED` | 1 | `` | [PlayerScript](systems/PlayerScript.md) |
| ✅ | `PLAYER_TOTEM_UPDATE` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `PLAYER_TRADE_CURRENCY` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `PLAYER_TRADE_MONEY` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `PLAYER_TRIAL_XP_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_UNGHOST` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `PLAYER_UPDATE_RESTING` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PLAYER_XP_UPDATE` | 2 | `s` | [Unit](systems/Unit.md) |
| 🆕 | `PLAYTIME_CHANGED` |  |  | used in `Blizzard_UnitFrame/Mainline/PlayerFrame.lua` |
| ✅ | `PLAY_MOVIE` |  |  | [Cinematic](systems/Cinematic.md) |
| ⛔ | `POINT` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `PORTRAITS_UPDATED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `POST_MATCH_CURRENCY_REWARD_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `POST_MATCH_ITEM_REWARD_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| 🆕 | `PREFERRED_PLAY_SETTINGS_UPDATED` | 1 | `n,n,n,n,n` | used in `Blizzard_Settings_Shared/Blizzard_Settings_PreferredPlaySettings.lua` |
| ⛔ | `PRIEST` |  |  | used in `Blizzard_FrameXMLBase/Camelot/Constants.lua` |
| 🆕 | `PRODUCT_ASSIGN_TO_TARGET_FAILED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `PRODUCT_DISTRIBUTIONS_UPDATED` |  |  | used in `Blizzard_ClassTrialSecure/Blizzard_ClassTrialSecure.lua` |
| ⛔ | `PROFESSIONS_SPECIALIZATION_CONFIRM_PURCHASE_TAB` |  |  | used in `Blizzard_Professions/Blizzard_ProfessionsSpecializations.lua` |
| ✅ | `PROFESSION_EQUIPMENT_CHANGED` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `PROFESSION_RESPEC_CONFIRMATION` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `PROVING_GROUNDS_SCORE_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ⛔ | `PROXY_ACCESSIBILITY_FONT_SIZE` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ⛔ | `PROXY_ADV_FLY_PITCH_CONTROL` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ⛔ | `PROXY_CENSOR_MESSAGES` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ⛔ | `PROXY_RAID_SPELL_DENSITY` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ⛔ | `PROXY_SHOW_ACTIONBAR_2` |  |  | used in `Blizzard_ActionBarController/ActionBarController.lua` |
| ⛔ | `PROXY_SHOW_ACTIONBAR_3` |  |  | used in `Blizzard_ActionBarController/ActionBarController.lua` |
| ⛔ | `PROXY_SHOW_ACTIONBAR_4` |  |  | used in `Blizzard_ActionBarController/ActionBarController.lua` |
| ⛔ | `PROXY_SHOW_ACTIONBAR_5` |  |  | used in `Blizzard_ActionBarController/ActionBarController.lua` |
| ⛔ | `PROXY_SHOW_ACTIONBAR_6` |  |  | used in `Blizzard_ActionBarController/ActionBarController.lua` |
| ⛔ | `PROXY_SHOW_ACTIONBAR_7` |  |  | used in `Blizzard_ActionBarController/ActionBarController.lua` |
| ⛔ | `PROXY_SHOW_ACTIONBAR_8` |  |  | used in `Blizzard_ActionBarController/ActionBarController.lua` |
| ⛔ | `PROXY_SPELL_DENSITY` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ✅ | `PURCHASE_PLOT_RESULT` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `PVPQUEUE_ANYWHERE_SHOW` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVPQUEUE_ANYWHERE_UPDATE_AVAILABLE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_BRAWL_INFO_UPDATED` | 1 | `` | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_MATCH_ACTIVE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_MATCH_COMPLETE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_MATCH_INACTIVE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_MATCH_STATE_CHANGED` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_POWER_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `PVP_RATED_STATS_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_REWARDS_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_ROLE_POPUP_HIDE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_ROLE_POPUP_SHOW` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_ROLE_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_SPECIAL_EVENT_INFO_UPDATED` | 1 | `` | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_TIMER_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `PVP_TYPES_ENABLED` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_VEHICLE_INFO_UPDATED` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `PVP_WORLDSTATE_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `QUESTLINE_UPDATE` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_ACCEPTED` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_ACCEPT_CONFIRM` |  |  | [QuestOffer](systems/QuestOffer.md) |
| ✅ | `QUEST_AUTOCOMPLETE` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_BOSS_EMOTE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `QUEST_COMPLETE` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_CURRENCY_LOOT_RECEIVED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `QUEST_DATA_LOAD_RESULT` | 24 | `n,b` | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_DETAIL` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_FINISHED` |  |  | [QuestOffer](systems/QuestOffer.md) |
| ✅ | `QUEST_GREETING` |  |  | [QuestOffer](systems/QuestOffer.md) |
| ✅ | `QUEST_ITEM_UPDATE` |  |  | [QuestOffer](systems/QuestOffer.md) |
| ✅ | `QUEST_LOG_CRITERIA_UPDATE` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_LOG_UPDATE` | 1 | `` | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_LOOT_RECEIVED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `QUEST_POI_UPDATE` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_PROGRESS` |  |  | [QuestOffer](systems/QuestOffer.md) |
| ✅ | `QUEST_REMOVED` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_SESSION_CREATED` |  |  | [QuestSession](systems/QuestSession.md) |
| ✅ | `QUEST_SESSION_DESTROYED` |  |  | [QuestSession](systems/QuestSession.md) |
| ✅ | `QUEST_SESSION_ENABLED_STATE_CHANGED` |  |  | [QuestSession](systems/QuestSession.md) |
| ✅ | `QUEST_SESSION_JOINED` |  |  | [QuestSession](systems/QuestSession.md) |
| ✅ | `QUEST_SESSION_LEFT` |  |  | [QuestSession](systems/QuestSession.md) |
| ✅ | `QUEST_SESSION_MEMBER_CONFIRM` |  |  | [QuestSession](systems/QuestSession.md) |
| ✅ | `QUEST_SESSION_MEMBER_START_RESPONSE` |  |  | [QuestSession](systems/QuestSession.md) |
| ✅ | `QUEST_SESSION_NOTIFICATION` |  |  | [QuestSession](systems/QuestSession.md) |
| ✅ | `QUEST_TURNED_IN` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_WATCH_LIST_CHANGED` | 1 | `-,-` | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUEST_WATCH_UPDATE` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `QUICK_TICKET_SYSTEM_STATUS` |  |  | [GMTicketInfo](systems/GMTicketInfo.md) |
| ✅ | `QUICK_TICKET_THROTTLE_CHANGED` |  |  | [GMTicketInfo](systems/GMTicketInfo.md) |
| 🆕 | `RACE_FACTION_CHANGE_RESULT` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| 🆕 | `RACE_FACTION_CHANGE_STARTED` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| ✅ | `RAF_ENTITLEMENT_DELIVERED` |  |  | [WowEntitlementInfo](systems/WowEntitlementInfo.md) |
| ✅ | `RAF_INFO_UPDATED` |  |  | [RecruitAFriend](systems/RecruitAFriend.md) |
| ✅ | `RAF_RECRUITING_ENABLED_STATUS` |  |  | [RecruitAFriend](systems/RecruitAFriend.md) |
| ✅ | `RAF_REWARD_CLAIM_FAILED` |  |  | [RecruitAFriend](systems/RecruitAFriend.md) |
| ✅ | `RAF_SYSTEM_ENABLED_STATUS` |  |  | [RecruitAFriend](systems/RecruitAFriend.md) |
| ✅ | `RAF_SYSTEM_INFO_UPDATED` |  |  | [RecruitAFriend](systems/RecruitAFriend.md) |
| ✅ | `RAID_BOSS_EMOTE` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `RAID_BOSS_WHISPER` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `RAID_INSTANCE_WELCOME` |  |  | [ChatInfo](systems/ChatInfo.md) |
| ⛔ | `RAID_LEADER` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ⛔ | `RAID_LOCKED` |  |  | used in `Blizzard_GroupFinder/Shared/LFGFrame.lua` |
| ✅ | `RAID_ROSTER_UPDATE` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `RAID_TARGET_UPDATE` |  |  | [EncounterInfo](systems/EncounterInfo.md) |
| ⛔ | `RAID_WARNING` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `RAISED_AS_GHOUL` |  |  | [PetInfo](systems/PetInfo.md) |
| 🆕 | `RANDOM_CHARACTER_NAME_RESULT` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| ✅ | `READY_CHECK` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `READY_CHECK_CONFIRM` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `READY_CHECK_FINISHED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| 🆕 | `REALM_HIDDEN_INFO_UPDATE` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `REALM_LIST_UPDATED` |  |  | used in `Blizzard_GlueXML/Mainline/RealmList.lua` |
| ✅ | `RECEIVED_ACHIEVEMENT_LIST` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `RECEIVED_ACHIEVEMENT_MEMBER_LIST` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `RECEIVED_HOUSE_LEVEL_REWARDS` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `RECENT_ALLIES_CACHE_UPDATE` |  |  | [RecentAllies](systems/RecentAllies.md) |
| ✅ | `RECENT_ALLIES_DATA_READY` |  |  | [RecentAllies](systems/RecentAllies.md) |
| ✅ | `RECENT_ALLIES_SYSTEM_STATUS_UPDATED` |  |  | [RecentAllies](systems/RecentAllies.md) |
| ✅ | `RECENT_ALLY_DATA_UPDATED` |  |  | [RecentAllies](systems/RecentAllies.md) |
| ✅ | `REJECTED_MATCHMAKING_PARTY_INVITE` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `REMIX_ARTIFACT_ITEM_SPECS_LOADED` |  |  | [RemixArtifactUI](systems/RemixArtifactUI.md) |
| ✅ | `REMIX_ARTIFACT_UPDATE` |  |  | [RemixArtifactUI](systems/RemixArtifactUI.md) |
| ✅ | `REMIX_END_OF_EVENT` |  |  | [TimerunningUI](systems/TimerunningUI.md) |
| ✅ | `REMOVE_NEIGHBORHOOD_CHARTER_SIGNATURE` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `REPLACE_ENCHANT` |  |  | [Item](systems/Item.md) |
| ✅ | `REPLACE_TRADESKILL_ENCHANT` |  |  | [Item](systems/Item.md) |
| ✅ | `REPLICATE_ITEM_LIST_UPDATE` |  |  | [AuctionHouse](systems/AuctionHouse.md) |
| ✅ | `REPORT_PLAYER_RESULT` |  |  | [ReportSystem](systems/ReportSystem.md) |
| ✅ | `REPORT_SCREENSHOT_READY` |  |  | [ReportSystem](systems/ReportSystem.md) |
| ✅ | `REQUESTED_GUILD_RENAME_RESULT` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `REQUEST_CEMETERY_LIST_RESPONSE` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ⛔ | `REQUEST_INVITE` |  |  | used in `Blizzard_FriendsFrame/Mainline/FriendsListUtil.lua` |
| ✅ | `REQUEST_INVITE_CONFIRMATION` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ⛔ | `REQUEST_INVITE_CROSS_FACTION` |  |  | used in `Blizzard_FriendsFrame/Mainline/FriendsListUtil.lua` |
| ✅ | `REQUIRED_GUILD_RENAME_RESULT` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `RESEARCH_ARTIFACT_COMPLETE` |  |  | [ResearchInfo](systems/ResearchInfo.md) |
| ✅ | `RESEARCH_ARTIFACT_DIG_SITE_UPDATED` |  |  | [ResearchInfo](systems/ResearchInfo.md) |
| ✅ | `RESEARCH_ARTIFACT_UPDATE` |  |  | [ResearchInfo](systems/ResearchInfo.md) |
| ✅ | `RESURRECT_REQUEST` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ⛔ | `REVEAL_CAPTURE_TOGGLED` |  |  | used in `Blizzard_Console/Blizzard_Console.lua` |
| ⛔ | `ROGUE` |  |  | used in `Blizzard_FrameXMLBase/Camelot/Constants.lua` |
| ✅ | `ROLE_CHANGED_INFORM` |  |  | [UnitRole](systems/UnitRole.md) |
| ✅ | `ROLE_POLL_BEGIN` |  |  | [UnitRole](systems/UnitRole.md) |
| ✅ | `RUNEFORGE_LEGENDARY_CRAFTING_CLOSED` |  |  | [LegendaryCrafting](systems/LegendaryCrafting.md) |
| ✅ | `RUNEFORGE_LEGENDARY_CRAFTING_OPENED` |  |  | [LegendaryCrafting](systems/LegendaryCrafting.md) |
| ✅ | `RUNEFORGE_POWER_INFO_UPDATED` |  |  | [LegendaryCrafting](systems/LegendaryCrafting.md) |
| ✅ | `RUNE_POWER_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `RUNE_TYPE_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ⛔ | `SALUTE` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `SAVED_VARIABLES_TOO_LARGE` |  |  | [AddOns](systems/AddOns.md) |
| ✅ | `SCENARIO_BONUS_OBJECTIVE_COMPLETE` |  |  | [ScenarioInfo](systems/ScenarioInfo.md) |
| ✅ | `SCENARIO_BONUS_VISIBILITY_UPDATE` |  |  | [ScenarioInfo](systems/ScenarioInfo.md) |
| ✅ | `SCENARIO_COMPLETED` |  |  | [ScenarioInfo](systems/ScenarioInfo.md) |
| ✅ | `SCENARIO_CRITERIA_SHOW_STATE_UPDATE` |  |  | [ScenarioInfo](systems/ScenarioInfo.md) |
| ✅ | `SCENARIO_CRITERIA_UPDATE` |  |  | [ScenarioInfo](systems/ScenarioInfo.md) |
| ✅ | `SCENARIO_POI_UPDATE` |  |  | [ScenarioInfo](systems/ScenarioInfo.md) |
| ✅ | `SCENARIO_SPELL_UPDATE` |  |  | [ScenarioInfo](systems/ScenarioInfo.md) |
| ✅ | `SCENARIO_UPDATE` |  |  | [ScenarioInfo](systems/ScenarioInfo.md) |
| ✅ | `SCRAPPING_MACHINE_ITEM_ADDED` |  |  | [ScrappingMachineUI](systems/ScrappingMachineUI.md) |
| ✅ | `SCRAPPING_MACHINE_ITEM_REMOVED` |  |  | [ScrappingMachineUI](systems/ScrappingMachineUI.md) |
| ✅ | `SCRAPPING_MACHINE_PENDING_ITEM_CHANGED` |  |  | [ScrappingMachineUI](systems/ScrappingMachineUI.md) |
| ✅ | `SCRAPPING_MACHINE_SCRAPPING_FINISHED` |  |  | [ScrappingMachineUI](systems/ScrappingMachineUI.md) |
| ✅ | `SCREENSHOT_FAILED` |  |  | [Video](systems/Video.md) |
| ✅ | `SCREENSHOT_STARTED` |  |  | [Video](systems/Video.md) |
| ✅ | `SCREENSHOT_SUCCEEDED` |  |  | [Video](systems/Video.md) |
| 🆕 | `SCREEN_FIRST_DISPLAYED` |  |  | used in `Blizzard_GlueXML/Mainline/AccountLogin.lua` |
| ✅ | `SCRIPTED_ANIMATIONS_UPDATE` |  |  | [ScriptedAnimations](systems/ScriptedAnimations.md) |
| ✅ | `SEARCH_DB_LOADED` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `SECURE_TRANSFER_CANCEL` | 2 | `` | [SecureTransfer](systems/SecureTransfer.md) |
| ✅ | `SECURE_TRANSFER_CONFIRM_HOUSING_PURCHASE` |  |  | [SecureTransfer](systems/SecureTransfer.md) |
| ✅ | `SECURE_TRANSFER_CONFIRM_SEND_MAIL` |  |  | [SecureTransfer](systems/SecureTransfer.md) |
| ✅ | `SECURE_TRANSFER_CONFIRM_TAKE_MAIL_MONEY` |  |  | [SecureTransfer](systems/SecureTransfer.md) |
| ✅ | `SECURE_TRANSFER_CONFIRM_TRADE_ACCEPT` |  |  | [SecureTransfer](systems/SecureTransfer.md) |
| ✅ | `SECURE_TRANSFER_HOUSING_CURRENCY_PURCHASE_CONFIRMATION` |  |  | [SecureTransfer](systems/SecureTransfer.md) |
| ✅ | `SELECTED_LOADOUT_CHANGED` |  |  | [ClassTalents](systems/ClassTalents.md) |
| 🆕 | `SELECT_WOW_LABS_AREA_FAILED` |  |  | used in `Blizzard_WorldMap/WoWLabs/WM_WoWLabsAreaDataProvider.lua` |
| ✅ | `SELF_RES_SPELL_CHANGED` |  |  | [DeathInfo](systems/DeathInfo.md) |
| ✅ | `SEND_MAIL_COD_CHANGED` |  |  | [MailInfo](systems/MailInfo.md) |
| ✅ | `SEND_MAIL_MONEY_CHANGED` |  |  | [MailInfo](systems/MailInfo.md) |
| 🆕 | `SESSION_TIME_ALERT` |  |  | used in `Blizzard_BNet/Mainline/BNet.lua` |
| ✅ | `SETTINGS_HEADER_TEXT_UPDATE` |  |  | [GameRules](systems/GameRules.md) |
| ✅ | `SETTINGS_LOADED` | 1 | `` | [SettingsUtil](systems/SettingsUtil.md) |
| ✅ | `SETTINGS_PANEL_OPEN` |  |  | [SettingsUtil](systems/SettingsUtil.md) |
| ⛔ | `SET_COMMUNITY_MEMBER_NOTE` |  |  | used in `Blizzard_Communities/CommunitiesFrame.lua` |
| ✅ | `SET_SEEN_PRODUCTS` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ⛔ | `SHAMAN` |  |  | used in `Blizzard_FrameXMLBase/Camelot/Constants.lua` |
| ✅ | `SHARD_TRANSFER` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `SHARD_TRANSFER_CANCELLED` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `SHARD_TRANSFER_IMMINENT` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `SHIPMENT_CRAFTER_CLOSED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `SHIPMENT_CRAFTER_INFO` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `SHIPMENT_CRAFTER_OPENED` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `SHIPMENT_CRAFTER_REAGENT_UPDATE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| ✅ | `SHIPMENT_UPDATE` |  |  | [GarrisonInfo](systems/GarrisonInfo.md) |
| 🆕 | `SHOULD_RECONNECT_TO_REALM_LIST` |  |  | used in `Blizzard_GlueXML/Mainline/AccountLogin.lua` |
| 🆕 | `SHOW_ARROW_CALLOUT` |  |  | used in `Blizzard_ArrowCalloutFrame/ArrowCalloutFrame.lua` |
| ✅ | `SHOW_DELVES_COMPANION_CONFIGURATION_UI` |  |  | [DelvesUI](systems/DelvesUI.md) |
| ✅ | `SHOW_END_OF_MATCH_UI` |  |  | [EndOfMatchUI](systems/EndOfMatchUI.md) |
| ✅ | `SHOW_FACTION_SELECT_UI` |  |  | [Unit](systems/Unit.md) |
| ✅ | `SHOW_HYPERLINK_TOOLTIP` |  |  | [TooltipInfo](systems/TooltipInfo.md) |
| ✅ | `SHOW_JOURNEYS_UI` |  |  | [EncounterJournal](systems/EncounterJournal.md) |
| ✅ | `SHOW_LFG_EXPAND_SEARCH_PROMPT` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `SHOW_LOOT_TOAST` |  |  | [Loot](systems/Loot.md) |
| ✅ | `SHOW_LOOT_TOAST_LEGENDARY_LOOTED` |  |  | [Loot](systems/Loot.md) |
| ✅ | `SHOW_LOOT_TOAST_UPGRADE` |  |  | [Loot](systems/Loot.md) |
| ✅ | `SHOW_NEIGHBORHOOD_OWNERSHIP_TRANSFER_DIALOG` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `SHOW_NEW_PRODUCT_NOTIFICATION` |  |  | [CatalogShop](systems/CatalogShop.md) |
| ✅ | `SHOW_PARTY_POSE_UI` |  |  | [PartyPose](systems/PartyPose.md) |
| ✅ | `SHOW_PLAYER_EVICTED_DIALOG` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `SHOW_PVP_FACTION_LOOT_TOAST` |  |  | [Loot](systems/Loot.md) |
| ✅ | `SHOW_RATED_PVP_REWARD_TOAST` |  |  | [Loot](systems/Loot.md) |
| 🆕 | `SHOW_SERVER_ALERT` |  |  | used in `Blizzard_GlueXML/ServerAlert.lua` |
| ✅ | `SHOW_STAIR_DIRECTION_CONFIRMATION` |  |  | [HousingLayoutUI](systems/HousingLayoutUI.md) |
| ✅ | `SHOW_SUBSCRIPTION_INTERSTITIAL` |  |  | [Expansion](systems/Expansion.md) |
| ✅ | `SHOW_SUBTITLE` |  |  | [Cinematic](systems/Cinematic.md) |
| ✅ | `SIMPLE_BROWSER_POPUP` |  |  | [Browser](systems/Browser.md) |
| ✅ | `SIMPLE_BROWSER_SOCIAL_CALLBACK_INVOKED` |  |  | [Browser](systems/Browser.md) |
| ✅ | `SIMPLE_BROWSER_WEB_ERROR` |  |  | [Browser](systems/Browser.md) |
| ✅ | `SIMPLE_BROWSER_WEB_PROXY_FAILED` |  |  | [Browser](systems/Browser.md) |
| ✅ | `SIMPLE_CHECKOUT_CLOSED` |  |  | [Browser](systems/Browser.md) |
| ✅ | `SKILL_LINES_CHANGED` | 2 | `` | [SkillInfo](systems/SkillInfo.md) |
| ✅ | `SKILL_LINE_SPECS_RANKS_CHANGED` |  |  | [ProfessionSpecUI](systems/ProfessionSpecUI.md) |
| ✅ | `SKILL_LINE_SPECS_UNLOCKED` |  |  | [ProfessionSpecUI](systems/ProfessionSpecUI.md) |
| ⛔ | `SLEEP` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| 🆕 | `SOCIAL_CONTRACT_STATUS_UPDATE` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ⛔ | `SOCIAL_ENABLE_DISCORD_FUNCTIONALITY` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ✅ | `SOCIAL_QUEUE_CONFIG_UPDATED` |  |  | [SocialQueue](systems/SocialQueue.md) |
| ✅ | `SOCIAL_QUEUE_UPDATE` |  |  | [SocialQueue](systems/SocialQueue.md) |
| ✅ | `SOCIAL_UI_FRIENDS_LIST_SYSTEM_STATUS_UPDATED` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `SOCIAL_UI_RAID_LIST_SYSTEM_STATUS_UPDATED` |  |  | [PartyInfoSystemStatus](systems/PartyInfoSystemStatus.md) |
| ✅ | `SOCIAL_UI_SOCIAL_QUEUE_SYSTEM_STATUS_UPDATED` |  |  | [SocialQueueSystemStatus](systems/SocialQueueSystemStatus.md) |
| ✅ | `SOCIAL_UI_SYSTEM_STATUS_UPDATED` |  |  | [SocialUI](systems/SocialUI.md) |
| ✅ | `SOCKET_INFO_ACCEPT` |  |  | [ItemSocketInfo](systems/ItemSocketInfo.md) |
| ✅ | `SOCKET_INFO_BIND_CONFIRM` |  |  | [ItemSocketInfo](systems/ItemSocketInfo.md) |
| ✅ | `SOCKET_INFO_CLOSE` | 1 | `` | [ItemSocketInfo](systems/ItemSocketInfo.md) |
| ✅ | `SOCKET_INFO_FAILURE` |  |  | [ItemSocketInfo](systems/ItemSocketInfo.md) |
| ✅ | `SOCKET_INFO_REFUNDABLE_CONFIRM` |  |  | [ItemSocketInfo](systems/ItemSocketInfo.md) |
| ✅ | `SOCKET_INFO_SUCCESS` |  |  | [ItemSocketInfo](systems/ItemSocketInfo.md) |
| ✅ | `SOCKET_INFO_UI_EVENT_REGISTRATION_UPDATE` |  |  | [ItemSocketInfo](systems/ItemSocketInfo.md) |
| ✅ | `SOCKET_INFO_UPDATE` |  |  | [ItemSocketInfo](systems/ItemSocketInfo.md) |
| ✅ | `SOULBIND_ACTIVATED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_CONDUIT_COLLECTION_CLEARED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_CONDUIT_COLLECTION_REMOVED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_CONDUIT_COLLECTION_UPDATED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_CONDUIT_INSTALLED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_CONDUIT_UNINSTALLED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_FORGE_INTERACTION_ENDED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_FORGE_INTERACTION_STARTED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_NODE_LEARNED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_NODE_UNLEARNED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_NODE_UPDATED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_PATH_CHANGED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOULBIND_PENDING_CONDUIT_CHANGED` |  |  | [Soulbinds](systems/Soulbinds.md) |
| ✅ | `SOUNDKIT_FINISHED` |  |  | [Sound](systems/Sound.md) |
| ✅ | `SOUND_DEVICE_UPDATE` |  |  | [Sound](systems/Sound.md) |
| ✅ | `SPECIALIZATION_CHANGE_CAST_FAILED` |  |  | [ClassTalents](systems/ClassTalents.md) |
| 🆕 | `SPECTATE_BEGIN` |  |  | used in `Blizzard_ActionBar/WoWLabs/ActionButtonOverrides.lua` |
| 🆕 | `SPECTATE_END` |  |  | used in `Blizzard_ActionBar/WoWLabs/ActionButtonOverrides.lua` |
| 🆕 | `SPECTATE_TARGET_INFO_UPDATED` |  |  | used in `Blizzard_SpectateFrame/SpectateFrame.lua` |
| ✅ | `SPEC_INVOLUNTARILY_CHANGED` |  |  | [SpecializationInfo](systems/SpecializationInfo.md) |
| ✅ | `SPEED_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `SPELLS_CHANGED` | 1 | `` | [SpellBook](systems/SpellBook.md) |
| ✅ | `SPELL_ACTIVATION_OVERLAY_GLOW_HIDE` |  |  | [SpellActivationOverlay](systems/SpellActivationOverlay.md) |
| ✅ | `SPELL_ACTIVATION_OVERLAY_GLOW_SHOW` |  |  | [SpellActivationOverlay](systems/SpellActivationOverlay.md) |
| ✅ | `SPELL_ACTIVATION_OVERLAY_HIDE` | 36 | `-` | [SpellActivationOverlay](systems/SpellActivationOverlay.md) |
| ✅ | `SPELL_ACTIVATION_OVERLAY_SHOW` |  |  | [SpellActivationOverlay](systems/SpellActivationOverlay.md) |
| ✅ | `SPELL_CONFIRMATION_PROMPT` |  |  | [Unit](systems/Unit.md) |
| ✅ | `SPELL_CONFIRMATION_TIMEOUT` |  |  | [Unit](systems/Unit.md) |
| ✅ | `SPELL_DATA_LOAD_RESULT` | 6 | `n,b` | [Spell](systems/Spell.md) |
| ✅ | `SPELL_FLYOUT_UPDATE` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `SPELL_POWER_CHANGED` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `SPELL_PUSHED_TO_ACTIONBAR` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `SPELL_PUSHED_TO_FLYOUT_ON_ACTIONBAR` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `SPELL_RANGE_CHECK_UPDATE` |  |  | [Spell](systems/Spell.md) |
| 🆕 | `SPELL_SCRIPT_ERROR` |  |  | used in `Blizzard_Console/Blizzard_Console.lua` |
| ✅ | `SPELL_TEXT_UPDATE` |  |  | [Spell](systems/Spell.md) |
| ✅ | `SPELL_UPDATE_CHARGES` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `SPELL_UPDATE_COOLDOWN` | 30 | `n,-,-,-,-` / `n,-,n,n,-` | [SpellBook](systems/SpellBook.md) |
| ✅ | `SPELL_UPDATE_ICON` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `SPELL_UPDATE_USABLE` | 285 | `` | [SpellBook](systems/SpellBook.md) |
| ✅ | `SPELL_UPDATE_USES` |  |  | [SpellBook](systems/SpellBook.md) |
| ⛔ | `STAND` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `STARTER_BUILD_ACTIVATION_FAILED` |  |  | [ClassTalents](systems/ClassTalents.md) |
| ✅ | `START_AUTOREPEAT_SPELL` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `START_LOOT_ROLL` |  |  | [Loot](systems/Loot.md) |
| ✅ | `START_PLAYER_COUNTDOWN` |  |  | [WorldStateInfo](systems/WorldStateInfo.md) |
| ✅ | `START_TIMER` |  |  | [WorldStateInfo](systems/WorldStateInfo.md) |
| ✅ | `STOP_AUTOREPEAT_SPELL` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `STOP_MOVIE` |  |  | [Cinematic](systems/Cinematic.md) |
| ✅ | `STOP_TIMER_OF_TYPE` |  |  | [WorldStateInfo](systems/WorldStateInfo.md) |
| 🆕 | `STORE_BOOST_AUTO_CONSUMED` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| 🆕 | `STORE_CHARACTER_LIST_RECEIVED` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| 🆕 | `STORE_CONFIRM_PURCHASE` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| ✅ | `STORE_FRONT_STATE_UPDATED` |  |  | [AccountStore](systems/AccountStore.md) |
| 🆕 | `STORE_GUILD_FOLLOW_INFO_RECEIVED` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| 🆕 | `STORE_GUILD_MASTER_INFO_RECEIVED` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| 🆕 | `STORE_OPEN_SIMPLE_CHECKOUT` |  |  | used in `Blizzard_SimpleCheckout/Blizzard_SimpleCheckout.lua` |
| 🆕 | `STORE_ORDER_INITIATION_FAILED` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| 🆕 | `STORE_PRODUCTS_UPDATED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `STORE_PURCHASE_ERROR` |  |  | used in `Blizzard_CatalogShop/Blizzard_CatalogShop.lua` |
| 🆕 | `STORE_PURCHASE_LIST_UPDATED` | 1 | `` | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| 🆕 | `STORE_REFRESH` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| 🆕 | `STORE_STATUS_CHANGED` |  |  | used in `Blizzard_GameMenu/Shared/GameMenuFrame.lua` |
| 🆕 | `STORE_VAS_PURCHASE_COMPLETE` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| 🆕 | `STORE_VAS_PURCHASE_ERROR` |  |  | used in `Blizzard_CharacterCreate/Camelot/Blizzard_CharacterCreate.lua` |
| ⛔ | `STRAFELEFT` |  |  | used in `Blizzard_NewPlayerExperience/Blizzard_TutorialKeyboardMouseFrame.lua` |
| ⛔ | `STRAFERIGHT` |  |  | used in `Blizzard_NewPlayerExperience/Blizzard_TutorialKeyboardMouseFrame.lua` |
| ✅ | `STREAMING_ICON` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `STREAM_VIEW_MARKER_UPDATED` |  |  | [Club](systems/Club.md) |
| ✅ | `STURDINESS_UPDATE` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| 🆕 | `SUBSCRIPTION_CHANGED_KICK_IMMINENT` |  |  | used in `Blizzard_GlueParent/Mainline/GlueParent.lua` |
| 🆕 | `SUBSCRIPTION_INTERSTITIAL_AVAILABLE` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `SUPER_DISTRICT_LIST_UPDATED` |  |  | used in `Blizzard_GlueXML/Mainline/SuperDistrict.lua` |
| ✅ | `SUPER_TRACKING_CHANGED` |  |  | [SuperTrackManager](systems/SuperTrackManager.md) |
| ✅ | `SUPER_TRACKING_PATH_UPDATED` |  |  | [SuperTrackManager](systems/SuperTrackManager.md) |
| ✅ | `SURVEY_DELIVERED` |  |  | [WowSurvey](systems/WowSurvey.md) |
| ✅ | `SYSMSG` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ⛔ | `SYSTEM` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `SYSTEM_VISIBILITY_CHANGED` |  |  | [UISystemVisibilityManager](systems/UISystemVisibilityManager.md) |
| ✅ | `TABARD_CANSAVE_CHANGED` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `TABARD_SAVE_PENDING` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `TALENTS_INVOLUNTARILY_RESET` |  |  | [SpecializationInfo](systems/SpecializationInfo.md) |
| ✅ | `TALKINGHEAD_CLOSE` |  |  | [TalkingHead](systems/TalkingHead.md) |
| ✅ | `TALKINGHEAD_REQUESTED` |  |  | [TalkingHead](systems/TalkingHead.md) |
| ✅ | `TASK_PROGRESS_UPDATE` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `TAXIMAP_CLOSED` | 1 | `` | [TaxiMap](systems/TaxiMap.md) |
| ✅ | `TAXIMAP_OPENED` |  |  | [TaxiMap](systems/TaxiMap.md) |
| ✅ | `TAXI_NODE_STATUS_CHANGED` |  |  | [TaxiMap](systems/TaxiMap.md) |
| ⛔ | `THANK` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| 🆕 | `TIMERUNNING_SEASON_UPDATE` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `TIME_PLAYED_MSG` | 1 | `n,n` | [SystemInfo](systems/SystemInfo.md) |
| ⛔ | `TOGGLEPINGTARGET` |  |  | used in `Blizzard_Settings_Shared/Mainline/NewDefinitions.lua` |
| ✅ | `TOGGLE_CONSOLE` |  |  | [Console](systems/Console.md) |
| 🆕 | `TOGGLE_FRAMESTACK` |  |  | used in `Blizzard_FrameStack/FrameStack.lua` |
| ⛔ | `TOKEN_AUCTIONABLE_TOKEN_OWNED` |  |  | used in `Blizzard_AuctionHouseUI/Shared/Blizzard_AuctionHouseFrame.lua` |
| ✅ | `TOKEN_AUCTION_SOLD` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_BUY_CONFIRM_REQUIRED` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_BUY_RESULT` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_CAN_VETERAN_BUY_UPDATE` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_DISTRIBUTIONS_UPDATED` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_MARKET_PRICE_UPDATED` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ⛔ | `TOKEN_NONE_FOR_SALE` |  |  | used in `Blizzard_AuctionHouseUI/Shared/Blizzard_AuctionHouseFrame.lua` |
| ✅ | `TOKEN_REDEEM_BALANCE_UPDATED` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_REDEEM_CONFIRM_REQUIRED` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_REDEEM_FRAME_SHOW` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_REDEEM_GAME_TIME_UPDATED` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_REDEEM_RESULT` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_SELL_CONFIRMED` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_SELL_CONFIRM_REQUIRED` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_SELL_RESULT` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOKEN_STATUS_CHANGED` |  |  | [WowTokenUI](systems/WowTokenUI.md) |
| ✅ | `TOOLTIP_DATA_UPDATE` |  |  | [TooltipInfo](systems/TooltipInfo.md) |
| ⛔ | `TOOLTIP_SHOW_ITEM_COMPARISON` |  |  | [TooltipComparison](systems/TooltipComparison.md) |
| ✅ | `TOYS_UPDATED` | 1 | `-,-,-` | [ToyBoxInfo](systems/ToyBoxInfo.md) |
| ✅ | `TRACKABLE_INFO_UPDATE` |  |  | [ContentTracking](systems/ContentTracking.md) |
| ✅ | `TRACKED_ACHIEVEMENT_LIST_CHANGED` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `TRACKED_ACHIEVEMENT_UPDATE` |  |  | [AchievementInfo](systems/AchievementInfo.md) |
| ✅ | `TRACKED_HOUSE_CHANGED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `TRACKED_RECIPE_UPDATE` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRACKING_TARGET_INFO_UPDATE` |  |  | [ContentTracking](systems/ContentTracking.md) |
| ✅ | `TRADE_ACCEPT_UPDATE` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_CLOSED` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_CURRENCY_CHANGED` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_MONEY_CHANGED` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_PLAYER_ITEM_CHANGED` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_POTENTIAL_BIND_ENCHANT` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_POTENTIAL_REMOVE_TRANSMOG` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_REPLACE_ENCHANT` |  |  | [Item](systems/Item.md) |
| ✅ | `TRADE_REQUEST` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_REQUEST_CANCEL` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_SHOW` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_SKILL_CLOSE` | 1 | `` | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_CRAFTING_REAGENT_BONUS_TEXT_UPDATED` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_CRAFT_BEGIN` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_CURRENCY_REWARD_RESULT` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_DATA_SOURCE_CHANGED` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_DATA_SOURCE_CHANGING` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_DETAILS_UPDATE` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_FAVORITES_CHANGED` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_ITEM_CRAFTED_RESULT` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_ITEM_UPDATE` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_LIST_UPDATE` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_NAME_UPDATE` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_SKILL_SHOW` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `TRADE_TARGET_ITEM_CHANGED` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_UPDATE` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ✅ | `TRADE_UPDATE_WARNINGS` |  |  | [TradeInfo](systems/TradeInfo.md) |
| ⛔ | `TRAIN` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ✅ | `TRAINER_CLOSED` |  |  | [Trainer](systems/Trainer.md) |
| ✅ | `TRAINER_DESCRIPTION_UPDATE` |  |  | [Trainer](systems/Trainer.md) |
| ✅ | `TRAINER_SERVICE_INFO_NAME_UPDATE` |  |  | [Trainer](systems/Trainer.md) |
| ✅ | `TRAINER_SHOW` |  |  | [Trainer](systems/Trainer.md) |
| ✅ | `TRAINER_UPDATE` |  |  | [Trainer](systems/Trainer.md) |
| ✅ | `TRAINING_GROUNDS_ENABLED_STATUS_UPDATED` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `TRAIT_COND_INFO_CHANGED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_CONFIG_CREATED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_CONFIG_DELETED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_CONFIG_LIST_UPDATED` | 1 | `` | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_CONFIG_UPDATED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_NODE_CHANGED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_NODE_CHANGED_PARTIAL` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_NODE_ENTRY_UPDATED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_SUB_TREE_CHANGED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_SYSTEM_INTERACTION_STARTED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_SYSTEM_NPC_CLOSED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_TREE_CHANGED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRAIT_TREE_CURRENCY_INFO_UPDATED` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ✅ | `TRANSMOGRIFY_CLOSE` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOGRIFY_ITEM_UPDATE` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOGRIFY_OPEN` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOGRIFY_SUCCESS` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOGRIFY_UPDATE` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_COLLECTION_CAMERA_UPDATE` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_COLLECTION_ITEM_FAVORITE_UPDATE` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_COLLECTION_ITEM_UPDATE` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_COLLECTION_SOURCE_ADDED` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_COLLECTION_SOURCE_REMOVED` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_COLLECTION_UPDATED` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_COSMETIC_COLLECTION_SOURCE_ADDED` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_CUSTOM_SETS_CHANGED` |  |  | [EquipmentSet](systems/EquipmentSet.md) |
| ⛔ | `TRANSMOG_CUSTOM_SET_ALL_INVALID_APPEARANCES` |  |  | used in `Blizzard_FrameXML/WardrobeCustomSets.lua` |
| ⛔ | `TRANSMOG_CUSTOM_SET_CHECKING_APPEARANCES` |  |  | used in `Blizzard_FrameXML/WardrobeCustomSets.lua` |
| ⛔ | `TRANSMOG_CUSTOM_SET_CONFIRM_OVERWRITE` |  |  | used in `Blizzard_FrameXML/WardrobeCustomSets.lua` |
| ⛔ | `TRANSMOG_CUSTOM_SET_NAME` |  |  | used in `Blizzard_FrameXML/WardrobeCustomSets.lua` |
| ⛔ | `TRANSMOG_CUSTOM_SET_SOME_INVALID_APPEARANCES` |  |  | used in `Blizzard_FrameXML/WardrobeCustomSets.lua` |
| ✅ | `TRANSMOG_DISPLAYED_OUTFIT_CHANGED` |  |  | [TransmogOutfitInfo](systems/TransmogOutfitInfo.md) |
| ✅ | `TRANSMOG_OUTFITS_CHANGED` |  |  | [TransmogOutfitInfo](systems/TransmogOutfitInfo.md) |
| ⛔ | `TRANSMOG_OUTFIT_INVALID_NAME` |  |  | used in `Blizzard_Transmog/Blizzard_Transmog.lua` |
| ⛔ | `TRANSMOG_PENDING_CHANGES` |  |  | used in `Blizzard_Transmog/Blizzard_Transmog.lua` |
| ✅ | `TRANSMOG_SEARCH_UPDATED` | 4 | `n,-` | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_SETS_UPDATE_FAVORITE` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TRANSMOG_SOURCE_COLLECTABILITY_UPDATE` |  |  | [Transmogrify](systems/Transmogrify.md) |
| ✅ | `TREASURE_PICKER_CACHE_FLUSH` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `TRIAL_CAP_REACHED_MONEY` |  |  | [Loot](systems/Loot.md) |
| 🆕 | `TRIAL_STATUS_UPDATE` |  |  | used in `Blizzard_AuctionHouseUI/Shared/Blizzard_AuctionHouseWoWTokenFrame.lua` |
| ✅ | `TRY_PURCHASE_TO_NODE_PARTIAL_SUCCESS` |  |  | [SharedTraits](systems/SharedTraits.md) |
| ⛔ | `TURNLEFT` |  |  | used in `Blizzard_BoostTutorial/Blizzard_TutorialKeyboardMouseFrame.lua` |
| ⛔ | `TURNRIGHT` |  |  | used in `Blizzard_BoostTutorial/Blizzard_TutorialKeyboardMouseFrame.lua` |
| ✅ | `TUTORIAL_COMBAT_EVENT` |  |  | [Tutorial](systems/Tutorial.md) |
| ✅ | `TUTORIAL_HIGHLIGHT_SPELL` |  |  | [Tutorial](systems/Tutorial.md) |
| ✅ | `TUTORIAL_TRIGGER` |  |  | [Tutorial](systems/Tutorial.md) |
| ✅ | `TUTORIAL_UNHIGHLIGHT_SPELL` |  |  | [Tutorial](systems/Tutorial.md) |
| ✅ | `UI_ERROR_MESSAGE` | 21 | `n,s` | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `UI_ERROR_POPUP` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `UI_INFO_MESSAGE` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `UI_MODEL_SCENE_INFO_UPDATED` |  |  | [ModelInfo](systems/ModelInfo.md) |
| ✅ | `UI_SCALE_CHANGED` | 2 | `` | [UI](systems/UI.md) |
| ✅ | `UNIT_ABSORB_AMOUNT_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_AREA_CHANGED` | 3 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_ARENA_COOLDOWNS_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_ATTACK` | 1 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_ATTACK_POWER` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_ATTACK_SPEED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_AURA` | 10 | `s,t` | [UnitAuras](systems/UnitAuras.md) |
| ✅ | `UNIT_AURA_BLOCKED` |  |  | [UnitAuras](systems/UnitAuras.md) |
| ✅ | `UNIT_AURA_BLOCK_LIST_CLEARED` |  |  | [UnitAuras](systems/UnitAuras.md) |
| ✅ | `UNIT_CHEAT_TOGGLE_EVENT` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_CLASSIFICATION_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_COMBAT` | 96 | `s,s,s,S,n` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_CONNECTION` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_CTR_OPTIONS` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_DAMAGE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_DEFENSE` | 1 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_DIED` | 1 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_DISPLAYPOWER` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_DISTANCE_CHECK_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_ENTERED_VEHICLE` |  |  | [Vehicle](systems/Vehicle.md) |
| ✅ | `UNIT_ENTERING_VEHICLE` |  |  | [Vehicle](systems/Vehicle.md) |
| ✅ | `UNIT_EXITED_VEHICLE` |  |  | [Vehicle](systems/Vehicle.md) |
| ✅ | `UNIT_EXITING_VEHICLE` |  |  | [Vehicle](systems/Vehicle.md) |
| ✅ | `UNIT_FACTION` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_FLAGS` | 13 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_FORM_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_GUILD_LEVEL` |  |  | [GuildInfo](systems/GuildInfo.md) |
| ✅ | `UNIT_HAPPINESS` | 49 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_HEALTH` | 127 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_HEAL_ABSORB_AMOUNT_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_HEAL_PREDICTION` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_INVENTORY_CHANGED` | 2 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_IN_RANGE_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_LEVEL` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_LOOT` | 3 | `s,b` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_MANA` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_MAXHEALTH` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_MAXPOWER` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_MAX_HEALTH_MODIFIERS_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_MODEL_CHANGED` | 1 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_NAME_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_OTHER_PARTY_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_PET` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_PET_EXPERIENCE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_PET_TRAINING_POINTS` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_PHASE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_PING_PIN_ADDED` |  |  | [PingManagerSecure](systems/PingManagerSecure.md) |
| ✅ | `UNIT_PING_PIN_REMOVED` |  |  | [PingManagerSecure](systems/PingManagerSecure.md) |
| ✅ | `UNIT_PORTRAIT_UPDATE` | 1 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_POWER_BAR_HIDE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_POWER_BAR_SHOW` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_POWER_BAR_TIMER_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_POWER_FREQUENT` | 402 | `s,s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_POWER_POINT_CHARGE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_POWER_UPDATE` | 64 | `s,s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_QUEST_LOG_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_RANGEDDAMAGE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_RANGED_ATTACK_POWER` | 1 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_RESISTANCES` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_CHANNEL_START` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_CHANNEL_STOP` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_CHANNEL_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_DELAYED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_EMPOWER_START` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_EMPOWER_STOP` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_EMPOWER_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_FAILED` | 36 | `s,s,n,-` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_FAILED_QUIET` | 6 | `s,s,n,-` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_INTERRUPTED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_INTERRUPTIBLE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_NOT_INTERRUPTIBLE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_RETICLE_CLEAR` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_RETICLE_TARGET` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_SENT` | 22 | `s,s,s,n` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_START` | 1 | `s,s,n,s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_STOP` | 1 | `s,s,n,s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELLCAST_SUCCEEDED` | 14 | `s,s,n,-` / `s,s,n,s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_SPELL_DIMINISH_CATEGORY_STATE_UPDATED` |  |  | [SpellDiminishUI](systems/SpellDiminishUI.md) |
| ✅ | `UNIT_SPELL_HASTE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_STATS` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_TARGET` | 9 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_TARGETABLE_CHANGED` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UNIT_THREAT_LIST_UPDATE` | 47 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UNIT_THREAT_SITUATION_UPDATE` | 4 | `s` | [Unit](systems/Unit.md) |
| ✅ | `UPDATE_ACTIVE_BATTLEFIELD` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `UPDATE_ALL_UI_WIDGETS` |  |  | [UIWidgetManager](systems/UIWidgetManager.md) |
| ✅ | `UPDATE_BATTLEFIELD_SCORE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `UPDATE_BATTLEFIELD_STATUS` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `UPDATE_BINDINGS` | 5 | `` | [KeyBindings](systems/KeyBindings.md) |
| ✅ | `UPDATE_BONUS_ACTIONBAR` |  |  | [ActionBar](systems/ActionBar.md) |
| ✅ | `UPDATE_BULLETIN_BOARD_MEMBER_TYPE` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `UPDATE_BULLETIN_BOARD_ROSTER` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `UPDATE_BULLETIN_BOARD_ROSTER_STATUSES` |  |  | [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) |
| ✅ | `UPDATE_CHAT_COLOR` | 94 | `s,n,n,n` | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `UPDATE_CHAT_COLOR_NAME_BY_CLASS` | 94 | `s,b` | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `UPDATE_CHAT_WINDOWS` | 3 | `` | [ChatInfo](systems/ChatInfo.md) |
| ✅ | `UPDATE_EXHAUSTION` |  |  | [Unit](systems/Unit.md) |
| 🆕 | `UPDATE_EXPANSION_LEVEL` |  |  | used in `Blizzard_ClassTrial/Blizzard_ClassTrial.lua` |
| ✅ | `UPDATE_EXTRA_ACTIONBAR` | 1 | `` | [ActionBar](systems/ActionBar.md) |
| ✅ | `UPDATE_FACTION` | 4 | `` | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `UPDATE_FLOATING_CHAT_WINDOWS` | 2 | `` | [ChatInfo](systems/ChatInfo.md) |
| 🆕 | `UPDATE_GM_STATUS` |  |  | used in `Blizzard_HelpFrame/HelpFrame.lua` |
| ✅ | `UPDATE_INSTANCE_INFO` | 3 | `` | [EncounterInfo](systems/EncounterInfo.md) |
| ✅ | `UPDATE_INVENTORY_ALERTS` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `UPDATE_INVENTORY_DURABILITY` | 2 | `` | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `UPDATE_LFG_LIST` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `UPDATE_MACROS` | 2 | `` | [UIMacros](systems/UIMacros.md) |
| ✅ | `UPDATE_MASTER_LOOT_LIST` |  |  | [Loot](systems/Loot.md) |
| ✅ | `UPDATE_MOUSEOVER_UNIT` | 9 | `` | [Unit](systems/Unit.md) |
| ✅ | `UPDATE_MULTI_CAST_ACTIONBAR` |  |  | [ActionBar](systems/ActionBar.md) |
| ✅ | `UPDATE_OVERRIDE_ACTIONBAR` | 1 | `` | [ActionBar](systems/ActionBar.md) |
| ✅ | `UPDATE_PENDING_MAIL` | 1 | `` | [MailInfo](systems/MailInfo.md) |
| ✅ | `UPDATE_POSSESS_BAR` |  |  | [PetInfo](systems/PetInfo.md) |
| 🆕 | `UPDATE_REALM_NAME_FOR_GUID` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect/CharacterSelectList.lua` |
| 🆕 | `UPDATE_SELECTED_CHARACTER` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `UPDATE_SHAPESHIFT_COOLDOWN` | 30 | `` | [SpellBook](systems/SpellBook.md) |
| ✅ | `UPDATE_SHAPESHIFT_FORM` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `UPDATE_SHAPESHIFT_FORMS` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `UPDATE_SHAPESHIFT_USABLE` |  |  | [SpellBook](systems/SpellBook.md) |
| ✅ | `UPDATE_SPELL_TARGET_ITEM_CONTEXT` |  |  | [Spell](systems/Spell.md) |
| ✅ | `UPDATE_STEALTH` |  |  | [Unit](systems/Unit.md) |
| ✅ | `UPDATE_SUMMONPETS_ACTION` | 1 | `` | [PetJournalInfo](systems/PetJournalInfo.md) |
| ✅ | `UPDATE_TRADESKILL_CAST_STOPPED` |  |  | [TradeSkillUI](systems/TradeSkillUI.md) |
| ✅ | `UPDATE_UI_WIDGET` |  |  | [UIWidgetManager](systems/UIWidgetManager.md) |
| ✅ | `UPDATE_VEHICLE_ACTIONBAR` | 1 | `` | [PetInfo](systems/PetInfo.md) |
| ✅ | `UPDATE_WEB_TICKET` |  |  | [GMTicketInfo](systems/GMTicketInfo.md) |
| ✅ | `URL_TEXTURE_REQUEST_RESULT` |  |  | [TextureUtils](systems/TextureUtils.md) |
| ✅ | `USER_WAYPOINT_UPDATED` |  |  | [MapUI](systems/MapUI.md) |
| ✅ | `USE_BIND_CONFIRM` |  |  | [Item](systems/Item.md) |
| ✅ | `USE_COMBINED_BAGS_CHANGED` |  |  | [Container](systems/Container.md) |
| ✅ | `USE_GLYPH` |  |  | [GlyphInfo](systems/GlyphInfo.md) |
| ✅ | `USE_NO_REFUND_CONFIRM` |  |  | [Item](systems/Item.md) |
| ✅ | `VARIABLES_LOADED` | 1 | `` | [SystemInfo](systems/SystemInfo.md) |
| 🆕 | `VAS_CHARACTER_QUEUE_STATUS_UPDATE` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `VAS_CHARACTER_STATE_CHANGED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| 🆕 | `VAS_QUEUE_STATUS_UPDATE` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| 🆕 | `VAS_TRANSFER_VALIDATION_UPDATE` |  |  | used in `Blizzard_StoreUI/Blizzard_Shared_StoreUISecure.lua` |
| ✅ | `VEHICLE_ANGLE_SHOW` | 1 | `-` | [Vehicle](systems/Vehicle.md) |
| ✅ | `VEHICLE_ANGLE_UPDATE` |  |  | [Unit](systems/Unit.md) |
| ✅ | `VEHICLE_PASSENGERS_CHANGED` |  |  | [Vehicle](systems/Vehicle.md) |
| ✅ | `VEHICLE_POWER_SHOW` | 1 | `-` | [Vehicle](systems/Vehicle.md) |
| ✅ | `VEHICLE_UPDATE` |  |  | [Vehicle](systems/Vehicle.md) |
| ✅ | `VIEWED_TRANSMOG_OUTFIT_CHANGED` |  |  | [TransmogOutfitInfo](systems/TransmogOutfitInfo.md) |
| ✅ | `VIEWED_TRANSMOG_OUTFIT_SECONDARY_SLOTS_CHANGED` |  |  | [TransmogOutfitInfo](systems/TransmogOutfitInfo.md) |
| ✅ | `VIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED` |  |  | [TransmogOutfitInfo](systems/TransmogOutfitInfo.md) |
| ✅ | `VIEWED_TRANSMOG_OUTFIT_SLOT_OPTION_CHANGED` |  |  | [TransmogOutfitInfo](systems/TransmogOutfitInfo.md) |
| ✅ | `VIEWED_TRANSMOG_OUTFIT_SLOT_REFRESH` |  |  | [TransmogOutfitInfo](systems/TransmogOutfitInfo.md) |
| ✅ | `VIEWED_TRANSMOG_OUTFIT_SLOT_SAVE_SUCCESS` |  |  | [TransmogOutfitInfo](systems/TransmogOutfitInfo.md) |
| ✅ | `VIEW_HOUSES_LIST_RECIEVED` |  |  | [HousingUI](systems/HousingUI.md) |
| ✅ | `VIGNETTES_UPDATED` |  |  | [Vignette](systems/Vignette.md) |
| ✅ | `VIGNETTE_MINIMAP_UPDATED` |  |  | [Vignette](systems/Vignette.md) |
| ✅ | `VOICE_CHAT_ACTIVE_INPUT_DEVICE_UPDATED` | 1 | `` | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_ACTIVE_OUTPUT_DEVICE_UPDATED` | 1 | `` | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_ACTIVE_VOICE_PROVIDER_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_AUDIO_CAPTURE_ENERGY` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_AUDIO_CAPTURE_STARTED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_AUDIO_CAPTURE_STOPPED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_ACTIVATED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_DEACTIVATED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_DISPLAY_NAME_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_JOINED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_ACTIVE_STATE_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_ADDED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_ENERGY_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_GUID_UPDATED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_MUTE_FOR_ALL_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_MUTE_FOR_ME_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_REMOVED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_SILENCED_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_SPEAKING_STATE_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_STT_MESSAGE` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MEMBER_VOLUME_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_MUTE_STATE_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_PTT_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_REMOVED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_TRANSCRIBING_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_TRANSMIT_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CHANNEL_VOLUME_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_COMMUNICATION_MODE_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_CONNECTION_SUCCESS` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_DEAFENED_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_DISCORD_SETTINGS_UPDATED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_ERROR` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_INPUT_DEVICES_UPDATED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_LOGIN` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_LOGOUT` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_MUTED_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_OUTPUT_DEVICES_UPDATED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_PENDING_CHANNEL_JOIN_STATE` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_PTT_BUTTON_PRESSED_STATE_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_SILENCED_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_SPEAK_FOR_ME_ACTIVE_STATUS_UPDATED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_SPEAK_FOR_ME_FEATURE_STATUS_UPDATED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_TTS_PLAYBACK_BOOKMARK` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_TTS_PLAYBACK_FAILED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_TTS_PLAYBACK_FINISHED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_TTS_PLAYBACK_STARTED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_TTS_SPEAK_TEXT_UPDATE` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_TTS_VOICES_UPDATE` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_VAD_SETTINGS_UPDATED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_VOICE_PROVIDERS_AVAILABLE_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOICE_CHAT_VOICE_PROVIDER_CHANGED` |  |  | [VoiceChat](systems/VoiceChat.md) |
| ✅ | `VOTE_KICK_REASON_NEEDED` |  |  | [PartyInfo](systems/PartyInfo.md) |
| ✅ | `WALK_IN_DATA_UPDATE` |  |  | [DelvesUI](systems/DelvesUI.md) |
| 🆕 | `WARBAND_GROUP_SCENE_UPDATED` |  |  | used in `Blizzard_GlueXML/Mainline/CharacterSelect.lua` |
| ✅ | `WARBAND_SCENE_FAVORITES_UPDATED` |  |  | [WarbandSceneInfo](systems/WarbandSceneInfo.md) |
| ✅ | `WARFRONT_COMPLETED` |  |  | [LFGInfo](systems/LFGInfo.md) |
| ✅ | `WARGAME_INVITE_SENT` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `WARGAME_REQUESTED` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `WARGAME_REQUEST_RESPONSE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ⛔ | `WARLOCK` |  |  | used in `Blizzard_FrameXMLBase/Camelot/Constants.lua` |
| ⛔ | `WARRIOR` |  |  | used in `Blizzard_FrameXMLBase/Camelot/Constants.lua` |
| ✅ | `WAR_MODE_STATUS_UPDATE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `WAYPOINT_UPDATE` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `WEAPON_ENCHANT_CHANGED` |  |  | [Item](systems/Item.md) |
| ✅ | `WEAPON_SLOT_CHANGED` |  |  | [PaperDollInfo](systems/PaperDollInfo.md) |
| ✅ | `WEATHER_CHANGED` |  |  | [WeatherScript](systems/WeatherScript.md) |
| ✅ | `WEEKLY_REWARDS_ITEM_CHANGED` |  |  | [WeeklyRewards](systems/WeeklyRewards.md) |
| ✅ | `WEEKLY_REWARDS_UPDATE` |  |  | [WeeklyRewards](systems/WeeklyRewards.md) |
| ⛔ | `WELCOME` |  |  | used in `Blizzard_ChatFrameBase/Mainline/ChatEmoteConstants.lua` |
| ⛔ | `WHISPER` |  |  | used in `Blizzard_ChatFrame/Mainline/TextToSpeechFrameConstants.lua` |
| ✅ | `WHO_LIST_UPDATE` |  |  | [FriendList](systems/FriendList.md) |
| ✅ | `WORLD_CURSOR_TOOLTIP_UPDATE` | 16 | `n` | [Cursor](systems/Cursor.md) |
| ✅ | `WORLD_LOOT_OBJECT_INFO_UPDATED` |  |  | [WorldLootObject](systems/WorldLootObject.md) |
| ✅ | `WORLD_MAP_OPEN` |  |  | [MapUI](systems/MapUI.md) |
| ✅ | `WORLD_PVP_QUEUE` |  |  | [PvpInfo](systems/PvpInfo.md) |
| ✅ | `WORLD_QUEST_COMPLETED_BY_SPELL` |  |  | [QuestLog](systems/QuestLog.md) |
| ✅ | `WORLD_STATE_TIMER_START` |  |  | [WorldStateInfo](systems/WorldStateInfo.md) |
| ✅ | `WORLD_STATE_TIMER_STOP` |  |  | [WorldStateInfo](systems/WorldStateInfo.md) |
| 🆕 | `WOW_LABS_AREA_INFO_UPDATED` |  |  | used in `Blizzard_WorldMap/WoWLabs/WM_WoWLabsAreaDataProvider.lua` |
| 🆕 | `WOW_LABS_AREA_SELECTED` |  |  | used in `Blizzard_WorldMap/WoWLabs/WM_WoWLabsAreaDataProvider.lua` |
| 🆕 | `WOW_LABS_BACKPACK_SIZE_CHANGED` |  |  | used in `Blizzard_ItemBeltFrame/ItemBeltFrame.lua` |
| 🆕 | `WOW_LABS_DATA_BR_CIRCLE` |  |  | used in `Blizzard_SharedMapDataProviders/PlunderstormCircleDataProvider.lua` |
| 🆕 | `WOW_LABS_MATCH_STATE_UPDATED` |  |  | used in `Blizzard_PlunderstormPrematchUI/Blizzard_PlunderstormPrematchUI.lua` |
| ✅ | `WOW_MOUSE_NOT_FOUND` |  |  | [SystemInfo](systems/SystemInfo.md) |
| ✅ | `ZONE_CHANGED` |  |  | [MapUI](systems/MapUI.md) |
| ✅ | `ZONE_CHANGED_INDOORS` |  |  | [MapUI](systems/MapUI.md) |
| ✅ | `ZONE_CHANGED_NEW_AREA` |  |  | [MapUI](systems/MapUI.md) |
