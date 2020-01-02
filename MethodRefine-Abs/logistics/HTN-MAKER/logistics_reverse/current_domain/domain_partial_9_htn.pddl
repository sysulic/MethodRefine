( define ( domain logistics )
  ( :requirements :strips :typing :equality :htn )
  ( :types airplane city location obj truck )
  ( :predicates
    ( OBJ-AT ?a - OBJ ?b - LOCATION )
    ( TRUCK-AT ?c - TRUCK ?d - LOCATION )
    ( AIRPLANE-AT ?e - AIRPLANE ?f - LOCATION )
    ( IN-TRUCK ?g - OBJ ?h - TRUCK )
    ( IN-AIRPLANE ?i - OBJ ?j - AIRPLANE )
    ( IN-CITY ?k - LOCATION ?l - CITY )
    ( AIRPORT ?o - LOCATION )
  )
  ( :action !LOAD-TRUCK
    :parameters
    (
      ?obj - OBJ
      ?truck - TRUCK
      ?loc - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?truck ?loc ) ( OBJ-AT ?obj ?loc ) )
    :effect
    ( and ( not ( OBJ-AT ?obj ?loc ) ) ( IN-TRUCK ?obj ?truck ) )
  )
  ( :action !LOAD-AIRPLANE
    :parameters
    (
      ?obj - OBJ
      ?airplane - AIRPLANE
      ?loc - LOCATION
    )
    :precondition
    ( and ( OBJ-AT ?obj ?loc ) ( AIRPLANE-AT ?airplane ?loc ) )
    :effect
    ( and ( not ( OBJ-AT ?obj ?loc ) ) ( IN-AIRPLANE ?obj ?airplane ) )
  )
  ( :action !UNLOAD-TRUCK
    :parameters
    (
      ?obj - OBJ
      ?truck - TRUCK
      ?loc - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?truck ?loc ) ( IN-TRUCK ?obj ?truck ) )
    :effect
    ( and ( not ( IN-TRUCK ?obj ?truck ) ) ( OBJ-AT ?obj ?loc ) )
  )
  ( :action !UNLOAD-AIRPLANE
    :parameters
    (
      ?obj - OBJ
      ?airplane - AIRPLANE
      ?loc - LOCATION
    )
    :precondition
    ( and ( IN-AIRPLANE ?obj ?airplane ) ( AIRPLANE-AT ?airplane ?loc ) )
    :effect
    ( and ( not ( IN-AIRPLANE ?obj ?airplane ) ) ( OBJ-AT ?obj ?loc ) )
  )
  ( :action !DRIVE-TRUCK
    :parameters
    (
      ?truck - TRUCK
      ?loc-from - LOCATION
      ?loc-to - LOCATION
      ?city - CITY
    )
    :precondition
    ( and ( TRUCK-AT ?truck ?loc-from ) ( IN-CITY ?loc-from ?city ) ( IN-CITY ?loc-to ?city ) ( not ( = ?loc-from ?loc-to ) ) )
    :effect
    ( and ( not ( TRUCK-AT ?truck ?loc-from ) ) ( TRUCK-AT ?truck ?loc-to ) )
  )
  ( :action !FLY-AIRPLANE
    :parameters
    (
      ?airplane - AIRPLANE
      ?loc-from - LOCATION
      ?loc-to - LOCATION
    )
    :precondition
    ( and ( AIRPORT ?loc-from ) ( AIRPORT ?loc-to ) ( AIRPLANE-AT ?airplane ?loc-from ) ( not ( = ?loc-from ?loc-to ) ) )
    :effect
    ( and ( not ( AIRPLANE-AT ?airplane ?loc-from ) ) ( AIRPLANE-AT ?airplane ?loc-to ) )
  )
  ( :method DELIVER-PKG
    :parameters
    (
      ?obj - OBJ
      ?dst - LOCATION
    )
    :precondition
    ( and ( OBJ-AT ?obj ?dst ) )
    :subtasks
    (  )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_2 - OBJ
      ?auto_3 - LOCATION
    )
    :vars
    (
      ?auto_4 - TRUCK
    )
    :precondition
    ( and ( TRUCK-AT ?auto_4 ?auto_3 ) ( IN-TRUCK ?auto_2 ?auto_4 ) )
    :subtasks
    ( ( !UNLOAD-TRUCK ?auto_2 ?auto_4 ?auto_3 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_7 - OBJ
      ?auto_8 - LOCATION
    )
    :vars
    (
      ?auto_11 - TRUCK
      ?auto_13 - LOCATION
      ?auto_14 - CITY
    )
    :precondition
    ( and ( IN-TRUCK ?auto_7 ?auto_11 ) ( TRUCK-AT ?auto_11 ?auto_13 ) ( IN-CITY ?auto_13 ?auto_14 ) ( IN-CITY ?auto_8 ?auto_14 ) ( not ( = ?auto_8 ?auto_13 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_11 ?auto_13 ?auto_8 ?auto_14 )
      ( DELIVER-PKG ?auto_7 ?auto_8 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_16 - OBJ
      ?auto_17 - LOCATION
    )
    :vars
    (
      ?auto_20 - TRUCK
      ?auto_22 - LOCATION
      ?auto_21 - CITY
      ?auto_24 - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?auto_20 ?auto_22 ) ( IN-CITY ?auto_22 ?auto_21 ) ( IN-CITY ?auto_17 ?auto_21 ) ( not ( = ?auto_17 ?auto_22 ) ) ( TRUCK-AT ?auto_20 ?auto_24 ) ( OBJ-AT ?auto_16 ?auto_24 ) )
    :subtasks
    ( ( !LOAD-TRUCK ?auto_16 ?auto_20 ?auto_24 )
      ( DELIVER-PKG ?auto_16 ?auto_17 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_782 - OBJ
      ?auto_783 - LOCATION
    )
    :vars
    (
      ?auto_790 - LOCATION
      ?auto_786 - CITY
      ?auto_785 - LOCATION
      ?auto_787 - CITY
      ?auto_792 - LOCATION
      ?auto_791 - CITY
      ?auto_788 - TRUCK
      ?auto_794 - LOCATION
      ?auto_795 - CITY
    )
    :precondition
    ( and ( IN-CITY ?auto_790 ?auto_786 ) ( IN-CITY ?auto_783 ?auto_786 ) ( not ( = ?auto_783 ?auto_790 ) ) ( OBJ-AT ?auto_782 ?auto_790 ) ( IN-CITY ?auto_785 ?auto_787 ) ( IN-CITY ?auto_790 ?auto_787 ) ( not ( = ?auto_790 ?auto_785 ) ) ( IN-CITY ?auto_792 ?auto_791 ) ( IN-CITY ?auto_785 ?auto_791 ) ( not ( = ?auto_785 ?auto_792 ) ) ( TRUCK-AT ?auto_788 ?auto_794 ) ( IN-CITY ?auto_794 ?auto_795 ) ( IN-CITY ?auto_792 ?auto_795 ) ( not ( = ?auto_792 ?auto_794 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_788 ?auto_794 ?auto_792 ?auto_795 )
      ( DELIVER-PKG ?auto_782 ?auto_783 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_40 - OBJ
      ?auto_41 - LOCATION
    )
    :vars
    (
      ?auto_44 - AIRPLANE
    )
    :precondition
    ( and ( IN-AIRPLANE ?auto_40 ?auto_44 ) ( AIRPLANE-AT ?auto_44 ?auto_41 ) )
    :subtasks
    ( ( !UNLOAD-AIRPLANE ?auto_40 ?auto_44 ?auto_41 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_45 - OBJ
      ?auto_46 - LOCATION
    )
    :vars
    (
      ?auto_49 - AIRPLANE
      ?auto_51 - LOCATION
    )
    :precondition
    ( and ( IN-AIRPLANE ?auto_45 ?auto_49 ) ( AIRPORT ?auto_51 ) ( AIRPORT ?auto_46 ) ( AIRPLANE-AT ?auto_49 ?auto_51 ) ( not ( = ?auto_51 ?auto_46 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_49 ?auto_51 ?auto_46 )
      ( DELIVER-PKG ?auto_45 ?auto_46 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_53 - OBJ
      ?auto_54 - LOCATION
    )
    :vars
    (
      ?auto_57 - LOCATION
      ?auto_55 - AIRPLANE
      ?auto_59 - LOCATION
    )
    :precondition
    ( and ( AIRPORT ?auto_57 ) ( AIRPORT ?auto_54 ) ( AIRPLANE-AT ?auto_55 ?auto_57 ) ( not ( = ?auto_57 ?auto_54 ) ) ( OBJ-AT ?auto_53 ?auto_59 ) ( AIRPLANE-AT ?auto_55 ?auto_59 ) )
    :subtasks
    ( ( !LOAD-AIRPLANE ?auto_53 ?auto_55 ?auto_59 )
      ( DELIVER-PKG ?auto_53 ?auto_54 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1863 - OBJ
      ?auto_1864 - LOCATION
    )
    :vars
    (
      ?auto_1868 - LOCATION
      ?auto_1865 - LOCATION
      ?auto_1872 - LOCATION
      ?auto_1866 - LOCATION
      ?auto_1870 - LOCATION
      ?auto_1874 - LOCATION
      ?auto_1867 - AIRPLANE
    )
    :precondition
    ( and ( AIRPORT ?auto_1868 ) ( AIRPORT ?auto_1864 ) ( not ( = ?auto_1868 ?auto_1864 ) ) ( OBJ-AT ?auto_1863 ?auto_1868 ) ( AIRPORT ?auto_1865 ) ( not ( = ?auto_1865 ?auto_1868 ) ) ( AIRPORT ?auto_1872 ) ( not ( = ?auto_1872 ?auto_1865 ) ) ( AIRPORT ?auto_1866 ) ( not ( = ?auto_1866 ?auto_1872 ) ) ( AIRPORT ?auto_1870 ) ( not ( = ?auto_1870 ?auto_1866 ) ) ( AIRPORT ?auto_1874 ) ( AIRPLANE-AT ?auto_1867 ?auto_1874 ) ( not ( = ?auto_1874 ?auto_1870 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_1867 ?auto_1874 ?auto_1870 )
      ( DELIVER-PKG ?auto_1863 ?auto_1864 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_72 - OBJ
      ?auto_73 - LOCATION
    )
    :vars
    (
      ?auto_74 - LOCATION
      ?auto_76 - LOCATION
      ?auto_75 - AIRPLANE
      ?auto_81 - TRUCK
    )
    :precondition
    ( and ( AIRPORT ?auto_74 ) ( AIRPORT ?auto_73 ) ( not ( = ?auto_74 ?auto_73 ) ) ( AIRPORT ?auto_76 ) ( AIRPLANE-AT ?auto_75 ?auto_76 ) ( not ( = ?auto_76 ?auto_74 ) ) ( TRUCK-AT ?auto_81 ?auto_74 ) ( IN-TRUCK ?auto_72 ?auto_81 ) )
    :subtasks
    ( ( DELIVER-PKG ?auto_72 ?auto_74 )
      ( DELIVER-PKG ?auto_72 ?auto_73 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_82 - OBJ
      ?auto_83 - LOCATION
    )
    :vars
    (
      ?auto_87 - LOCATION
      ?auto_86 - LOCATION
      ?auto_88 - AIRPLANE
      ?auto_89 - TRUCK
      ?auto_91 - LOCATION
      ?auto_92 - CITY
    )
    :precondition
    ( and ( AIRPORT ?auto_87 ) ( AIRPORT ?auto_83 ) ( not ( = ?auto_87 ?auto_83 ) ) ( AIRPORT ?auto_86 ) ( AIRPLANE-AT ?auto_88 ?auto_86 ) ( not ( = ?auto_86 ?auto_87 ) ) ( IN-TRUCK ?auto_82 ?auto_89 ) ( TRUCK-AT ?auto_89 ?auto_91 ) ( IN-CITY ?auto_91 ?auto_92 ) ( IN-CITY ?auto_87 ?auto_92 ) ( not ( = ?auto_87 ?auto_91 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_89 ?auto_91 ?auto_87 ?auto_92 )
      ( DELIVER-PKG ?auto_82 ?auto_83 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_94 - OBJ
      ?auto_95 - LOCATION
    )
    :vars
    (
      ?auto_99 - LOCATION
      ?auto_100 - LOCATION
      ?auto_98 - AIRPLANE
      ?auto_96 - TRUCK
      ?auto_102 - LOCATION
      ?auto_103 - CITY
      ?auto_105 - LOCATION
    )
    :precondition
    ( and ( AIRPORT ?auto_99 ) ( AIRPORT ?auto_95 ) ( not ( = ?auto_99 ?auto_95 ) ) ( AIRPORT ?auto_100 ) ( AIRPLANE-AT ?auto_98 ?auto_100 ) ( not ( = ?auto_100 ?auto_99 ) ) ( TRUCK-AT ?auto_96 ?auto_102 ) ( IN-CITY ?auto_102 ?auto_103 ) ( IN-CITY ?auto_99 ?auto_103 ) ( not ( = ?auto_99 ?auto_102 ) ) ( TRUCK-AT ?auto_96 ?auto_105 ) ( OBJ-AT ?auto_94 ?auto_105 ) )
    :subtasks
    ( ( !LOAD-TRUCK ?auto_94 ?auto_96 ?auto_105 )
      ( DELIVER-PKG ?auto_94 ?auto_95 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_107 - OBJ
      ?auto_108 - LOCATION
    )
    :vars
    (
      ?auto_112 - LOCATION
      ?auto_111 - LOCATION
      ?auto_113 - AIRPLANE
      ?auto_110 - LOCATION
      ?auto_114 - CITY
      ?auto_109 - TRUCK
      ?auto_119 - LOCATION
      ?auto_120 - CITY
    )
    :precondition
    ( and ( AIRPORT ?auto_112 ) ( AIRPORT ?auto_108 ) ( not ( = ?auto_112 ?auto_108 ) ) ( AIRPORT ?auto_111 ) ( AIRPLANE-AT ?auto_113 ?auto_111 ) ( not ( = ?auto_111 ?auto_112 ) ) ( IN-CITY ?auto_110 ?auto_114 ) ( IN-CITY ?auto_112 ?auto_114 ) ( not ( = ?auto_112 ?auto_110 ) ) ( OBJ-AT ?auto_107 ?auto_110 ) ( TRUCK-AT ?auto_109 ?auto_119 ) ( IN-CITY ?auto_119 ?auto_120 ) ( IN-CITY ?auto_110 ?auto_120 ) ( not ( = ?auto_110 ?auto_119 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_109 ?auto_119 ?auto_110 ?auto_120 )
      ( DELIVER-PKG ?auto_107 ?auto_108 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_148 - OBJ
      ?auto_149 - LOCATION
    )
    :vars
    (
      ?auto_153 - TRUCK
      ?auto_150 - LOCATION
      ?auto_155 - CITY
      ?auto_152 - LOCATION
      ?auto_158 - AIRPLANE
    )
    :precondition
    ( and ( TRUCK-AT ?auto_153 ?auto_150 ) ( IN-CITY ?auto_150 ?auto_155 ) ( IN-CITY ?auto_149 ?auto_155 ) ( not ( = ?auto_149 ?auto_150 ) ) ( TRUCK-AT ?auto_153 ?auto_152 ) ( IN-AIRPLANE ?auto_148 ?auto_158 ) ( AIRPLANE-AT ?auto_158 ?auto_152 ) )
    :subtasks
    ( ( DELIVER-PKG ?auto_148 ?auto_152 )
      ( DELIVER-PKG ?auto_148 ?auto_149 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_159 - OBJ
      ?auto_160 - LOCATION
    )
    :vars
    (
      ?auto_163 - TRUCK
      ?auto_167 - LOCATION
      ?auto_164 - CITY
      ?auto_166 - LOCATION
      ?auto_161 - AIRPLANE
      ?auto_169 - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?auto_163 ?auto_167 ) ( IN-CITY ?auto_167 ?auto_164 ) ( IN-CITY ?auto_160 ?auto_164 ) ( not ( = ?auto_160 ?auto_167 ) ) ( TRUCK-AT ?auto_163 ?auto_166 ) ( IN-AIRPLANE ?auto_159 ?auto_161 ) ( AIRPORT ?auto_169 ) ( AIRPORT ?auto_166 ) ( AIRPLANE-AT ?auto_161 ?auto_169 ) ( not ( = ?auto_169 ?auto_166 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_161 ?auto_169 ?auto_166 )
      ( DELIVER-PKG ?auto_159 ?auto_160 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_171 - OBJ
      ?auto_172 - LOCATION
    )
    :vars
    (
      ?auto_173 - TRUCK
      ?auto_174 - LOCATION
      ?auto_180 - CITY
      ?auto_177 - LOCATION
      ?auto_179 - LOCATION
      ?auto_178 - AIRPLANE
      ?auto_181 - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?auto_173 ?auto_174 ) ( IN-CITY ?auto_174 ?auto_180 ) ( IN-CITY ?auto_172 ?auto_180 ) ( not ( = ?auto_172 ?auto_174 ) ) ( TRUCK-AT ?auto_173 ?auto_177 ) ( AIRPORT ?auto_179 ) ( AIRPORT ?auto_177 ) ( AIRPLANE-AT ?auto_178 ?auto_179 ) ( not ( = ?auto_179 ?auto_177 ) ) ( OBJ-AT ?auto_171 ?auto_181 ) ( AIRPLANE-AT ?auto_178 ?auto_181 ) )
    :subtasks
    ( ( !LOAD-AIRPLANE ?auto_171 ?auto_178 ?auto_181 )
      ( DELIVER-PKG ?auto_171 ?auto_172 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_2281 - OBJ
      ?auto_2282 - LOCATION
    )
    :vars
    (
      ?auto_2292 - TRUCK
      ?auto_2290 - LOCATION
      ?auto_2285 - CITY
      ?auto_2289 - LOCATION
      ?auto_2284 - LOCATION
      ?auto_2288 - LOCATION
      ?auto_2286 - LOCATION
      ?auto_2294 - LOCATION
      ?auto_2283 - AIRPLANE
    )
    :precondition
    ( and ( TRUCK-AT ?auto_2292 ?auto_2290 ) ( IN-CITY ?auto_2290 ?auto_2285 ) ( IN-CITY ?auto_2282 ?auto_2285 ) ( not ( = ?auto_2282 ?auto_2290 ) ) ( TRUCK-AT ?auto_2292 ?auto_2289 ) ( AIRPORT ?auto_2284 ) ( AIRPORT ?auto_2289 ) ( not ( = ?auto_2284 ?auto_2289 ) ) ( OBJ-AT ?auto_2281 ?auto_2284 ) ( AIRPORT ?auto_2288 ) ( not ( = ?auto_2288 ?auto_2284 ) ) ( AIRPORT ?auto_2286 ) ( not ( = ?auto_2286 ?auto_2288 ) ) ( AIRPORT ?auto_2294 ) ( AIRPLANE-AT ?auto_2283 ?auto_2294 ) ( not ( = ?auto_2294 ?auto_2286 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_2283 ?auto_2294 ?auto_2286 )
      ( DELIVER-PKG ?auto_2281 ?auto_2282 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_198 - OBJ
      ?auto_199 - LOCATION
    )
    :vars
    (
      ?auto_202 - TRUCK
      ?auto_203 - LOCATION
      ?auto_206 - CITY
      ?auto_204 - LOCATION
      ?auto_205 - LOCATION
      ?auto_208 - LOCATION
      ?auto_207 - AIRPLANE
      ?auto_211 - TRUCK
    )
    :precondition
    ( and ( TRUCK-AT ?auto_202 ?auto_203 ) ( IN-CITY ?auto_203 ?auto_206 ) ( IN-CITY ?auto_199 ?auto_206 ) ( not ( = ?auto_199 ?auto_203 ) ) ( TRUCK-AT ?auto_202 ?auto_204 ) ( AIRPORT ?auto_205 ) ( AIRPORT ?auto_204 ) ( not ( = ?auto_205 ?auto_204 ) ) ( AIRPORT ?auto_208 ) ( AIRPLANE-AT ?auto_207 ?auto_208 ) ( not ( = ?auto_208 ?auto_205 ) ) ( TRUCK-AT ?auto_211 ?auto_205 ) ( IN-TRUCK ?auto_198 ?auto_211 ) )
    :subtasks
    ( ( DELIVER-PKG ?auto_198 ?auto_205 )
      ( DELIVER-PKG ?auto_198 ?auto_199 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_212 - OBJ
      ?auto_213 - LOCATION
    )
    :vars
    (
      ?auto_217 - TRUCK
      ?auto_215 - LOCATION
      ?auto_222 - CITY
      ?auto_220 - LOCATION
      ?auto_223 - LOCATION
      ?auto_221 - LOCATION
      ?auto_219 - AIRPLANE
      ?auto_218 - TRUCK
      ?auto_225 - LOCATION
      ?auto_226 - CITY
    )
    :precondition
    ( and ( TRUCK-AT ?auto_217 ?auto_215 ) ( IN-CITY ?auto_215 ?auto_222 ) ( IN-CITY ?auto_213 ?auto_222 ) ( not ( = ?auto_213 ?auto_215 ) ) ( TRUCK-AT ?auto_217 ?auto_220 ) ( AIRPORT ?auto_223 ) ( AIRPORT ?auto_220 ) ( not ( = ?auto_223 ?auto_220 ) ) ( AIRPORT ?auto_221 ) ( AIRPLANE-AT ?auto_219 ?auto_221 ) ( not ( = ?auto_221 ?auto_223 ) ) ( IN-TRUCK ?auto_212 ?auto_218 ) ( TRUCK-AT ?auto_218 ?auto_225 ) ( IN-CITY ?auto_225 ?auto_226 ) ( IN-CITY ?auto_223 ?auto_226 ) ( not ( = ?auto_223 ?auto_225 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_218 ?auto_225 ?auto_223 ?auto_226 )
      ( DELIVER-PKG ?auto_212 ?auto_213 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_228 - OBJ
      ?auto_229 - LOCATION
    )
    :vars
    (
      ?auto_239 - TRUCK
      ?auto_231 - LOCATION
      ?auto_238 - CITY
      ?auto_235 - LOCATION
      ?auto_234 - LOCATION
      ?auto_236 - LOCATION
      ?auto_237 - AIRPLANE
      ?auto_230 - TRUCK
      ?auto_240 - LOCATION
      ?auto_241 - CITY
      ?auto_243 - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?auto_239 ?auto_231 ) ( IN-CITY ?auto_231 ?auto_238 ) ( IN-CITY ?auto_229 ?auto_238 ) ( not ( = ?auto_229 ?auto_231 ) ) ( TRUCK-AT ?auto_239 ?auto_235 ) ( AIRPORT ?auto_234 ) ( AIRPORT ?auto_235 ) ( not ( = ?auto_234 ?auto_235 ) ) ( AIRPORT ?auto_236 ) ( AIRPLANE-AT ?auto_237 ?auto_236 ) ( not ( = ?auto_236 ?auto_234 ) ) ( TRUCK-AT ?auto_230 ?auto_240 ) ( IN-CITY ?auto_240 ?auto_241 ) ( IN-CITY ?auto_234 ?auto_241 ) ( not ( = ?auto_234 ?auto_240 ) ) ( TRUCK-AT ?auto_230 ?auto_243 ) ( OBJ-AT ?auto_228 ?auto_243 ) )
    :subtasks
    ( ( !LOAD-TRUCK ?auto_228 ?auto_230 ?auto_243 )
      ( DELIVER-PKG ?auto_228 ?auto_229 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_245 - OBJ
      ?auto_246 - LOCATION
    )
    :vars
    (
      ?auto_252 - TRUCK
      ?auto_258 - LOCATION
      ?auto_254 - CITY
      ?auto_255 - LOCATION
      ?auto_249 - LOCATION
      ?auto_256 - LOCATION
      ?auto_253 - AIRPLANE
      ?auto_259 - LOCATION
      ?auto_250 - CITY
      ?auto_257 - TRUCK
      ?auto_261 - LOCATION
      ?auto_262 - CITY
    )
    :precondition
    ( and ( TRUCK-AT ?auto_252 ?auto_258 ) ( IN-CITY ?auto_258 ?auto_254 ) ( IN-CITY ?auto_246 ?auto_254 ) ( not ( = ?auto_246 ?auto_258 ) ) ( TRUCK-AT ?auto_252 ?auto_255 ) ( AIRPORT ?auto_249 ) ( AIRPORT ?auto_255 ) ( not ( = ?auto_249 ?auto_255 ) ) ( AIRPORT ?auto_256 ) ( AIRPLANE-AT ?auto_253 ?auto_256 ) ( not ( = ?auto_256 ?auto_249 ) ) ( IN-CITY ?auto_259 ?auto_250 ) ( IN-CITY ?auto_249 ?auto_250 ) ( not ( = ?auto_249 ?auto_259 ) ) ( OBJ-AT ?auto_245 ?auto_259 ) ( TRUCK-AT ?auto_257 ?auto_261 ) ( IN-CITY ?auto_261 ?auto_262 ) ( IN-CITY ?auto_259 ?auto_262 ) ( not ( = ?auto_259 ?auto_261 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_257 ?auto_261 ?auto_259 ?auto_262 )
      ( DELIVER-PKG ?auto_245 ?auto_246 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_415 - OBJ
      ?auto_416 - LOCATION
    )
    :vars
    (
      ?auto_418 - LOCATION
      ?auto_417 - AIRPLANE
      ?auto_421 - LOCATION
      ?auto_423 - TRUCK
    )
    :precondition
    ( and ( AIRPORT ?auto_418 ) ( AIRPORT ?auto_416 ) ( AIRPLANE-AT ?auto_417 ?auto_418 ) ( not ( = ?auto_418 ?auto_416 ) ) ( AIRPLANE-AT ?auto_417 ?auto_421 ) ( TRUCK-AT ?auto_423 ?auto_421 ) ( IN-TRUCK ?auto_415 ?auto_423 ) )
    :subtasks
    ( ( DELIVER-PKG ?auto_415 ?auto_421 )
      ( DELIVER-PKG ?auto_415 ?auto_416 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_425 - OBJ
      ?auto_426 - LOCATION
    )
    :vars
    (
      ?auto_432 - LOCATION
      ?auto_431 - AIRPLANE
      ?auto_429 - LOCATION
      ?auto_427 - TRUCK
      ?auto_434 - LOCATION
      ?auto_435 - CITY
    )
    :precondition
    ( and ( AIRPORT ?auto_432 ) ( AIRPORT ?auto_426 ) ( AIRPLANE-AT ?auto_431 ?auto_432 ) ( not ( = ?auto_432 ?auto_426 ) ) ( AIRPLANE-AT ?auto_431 ?auto_429 ) ( IN-TRUCK ?auto_425 ?auto_427 ) ( TRUCK-AT ?auto_427 ?auto_434 ) ( IN-CITY ?auto_434 ?auto_435 ) ( IN-CITY ?auto_429 ?auto_435 ) ( not ( = ?auto_429 ?auto_434 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_427 ?auto_434 ?auto_429 ?auto_435 )
      ( DELIVER-PKG ?auto_425 ?auto_426 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_437 - OBJ
      ?auto_438 - LOCATION
    )
    :vars
    (
      ?auto_445 - LOCATION
      ?auto_442 - AIRPLANE
      ?auto_444 - LOCATION
      ?auto_439 - TRUCK
      ?auto_446 - LOCATION
      ?auto_443 - CITY
      ?auto_448 - LOCATION
    )
    :precondition
    ( and ( AIRPORT ?auto_445 ) ( AIRPORT ?auto_438 ) ( AIRPLANE-AT ?auto_442 ?auto_445 ) ( not ( = ?auto_445 ?auto_438 ) ) ( AIRPLANE-AT ?auto_442 ?auto_444 ) ( TRUCK-AT ?auto_439 ?auto_446 ) ( IN-CITY ?auto_446 ?auto_443 ) ( IN-CITY ?auto_444 ?auto_443 ) ( not ( = ?auto_444 ?auto_446 ) ) ( TRUCK-AT ?auto_439 ?auto_448 ) ( OBJ-AT ?auto_437 ?auto_448 ) )
    :subtasks
    ( ( !LOAD-TRUCK ?auto_437 ?auto_439 ?auto_448 )
      ( DELIVER-PKG ?auto_437 ?auto_438 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_461 - OBJ
      ?auto_462 - LOCATION
    )
    :vars
    (
      ?auto_463 - LOCATION
      ?auto_465 - AIRPLANE
      ?auto_464 - LOCATION
      ?auto_468 - LOCATION
      ?auto_467 - CITY
      ?auto_469 - TRUCK
      ?auto_473 - LOCATION
      ?auto_474 - CITY
    )
    :precondition
    ( and ( AIRPORT ?auto_463 ) ( AIRPORT ?auto_462 ) ( AIRPLANE-AT ?auto_465 ?auto_463 ) ( not ( = ?auto_463 ?auto_462 ) ) ( AIRPLANE-AT ?auto_465 ?auto_464 ) ( IN-CITY ?auto_468 ?auto_467 ) ( IN-CITY ?auto_464 ?auto_467 ) ( not ( = ?auto_464 ?auto_468 ) ) ( OBJ-AT ?auto_461 ?auto_468 ) ( TRUCK-AT ?auto_469 ?auto_473 ) ( IN-CITY ?auto_473 ?auto_474 ) ( IN-CITY ?auto_468 ?auto_474 ) ( not ( = ?auto_468 ?auto_473 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_469 ?auto_473 ?auto_468 ?auto_474 )
      ( DELIVER-PKG ?auto_461 ?auto_462 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_2695 - OBJ
      ?auto_2696 - LOCATION
    )
    :vars
    (
      ?auto_2705 - LOCATION
      ?auto_2698 - LOCATION
      ?auto_2700 - LOCATION
      ?auto_2706 - CITY
      ?auto_2701 - TRUCK
      ?auto_2703 - LOCATION
      ?auto_2702 - CITY
      ?auto_2699 - LOCATION
      ?auto_2697 - LOCATION
      ?auto_2708 - LOCATION
      ?auto_2711 - LOCATION
      ?auto_2709 - AIRPLANE
    )
    :precondition
    ( and ( AIRPORT ?auto_2705 ) ( AIRPORT ?auto_2696 ) ( not ( = ?auto_2705 ?auto_2696 ) ) ( AIRPORT ?auto_2698 ) ( not ( = ?auto_2698 ?auto_2705 ) ) ( IN-CITY ?auto_2700 ?auto_2706 ) ( IN-CITY ?auto_2705 ?auto_2706 ) ( not ( = ?auto_2705 ?auto_2700 ) ) ( OBJ-AT ?auto_2695 ?auto_2700 ) ( TRUCK-AT ?auto_2701 ?auto_2703 ) ( IN-CITY ?auto_2703 ?auto_2702 ) ( IN-CITY ?auto_2700 ?auto_2702 ) ( not ( = ?auto_2700 ?auto_2703 ) ) ( AIRPORT ?auto_2699 ) ( not ( = ?auto_2699 ?auto_2698 ) ) ( AIRPORT ?auto_2697 ) ( not ( = ?auto_2697 ?auto_2699 ) ) ( AIRPORT ?auto_2708 ) ( not ( = ?auto_2708 ?auto_2697 ) ) ( AIRPORT ?auto_2711 ) ( AIRPLANE-AT ?auto_2709 ?auto_2711 ) ( not ( = ?auto_2711 ?auto_2708 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_2709 ?auto_2711 ?auto_2708 )
      ( DELIVER-PKG ?auto_2695 ?auto_2696 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1042 - OBJ
      ?auto_1043 - LOCATION
    )
    :vars
    (
      ?auto_1048 - LOCATION
      ?auto_1044 - LOCATION
      ?auto_1049 - LOCATION
      ?auto_1047 - CITY
      ?auto_1054 - TRUCK
      ?auto_1050 - LOCATION
      ?auto_1052 - CITY
      ?auto_1053 - LOCATION
      ?auto_1055 - LOCATION
      ?auto_1057 - LOCATION
      ?auto_1046 - AIRPLANE
    )
    :precondition
    ( and ( AIRPORT ?auto_1048 ) ( AIRPORT ?auto_1043 ) ( not ( = ?auto_1048 ?auto_1043 ) ) ( AIRPORT ?auto_1044 ) ( not ( = ?auto_1044 ?auto_1048 ) ) ( IN-CITY ?auto_1049 ?auto_1047 ) ( IN-CITY ?auto_1048 ?auto_1047 ) ( not ( = ?auto_1048 ?auto_1049 ) ) ( OBJ-AT ?auto_1042 ?auto_1049 ) ( TRUCK-AT ?auto_1054 ?auto_1050 ) ( IN-CITY ?auto_1050 ?auto_1052 ) ( IN-CITY ?auto_1049 ?auto_1052 ) ( not ( = ?auto_1049 ?auto_1050 ) ) ( AIRPORT ?auto_1053 ) ( not ( = ?auto_1053 ?auto_1044 ) ) ( AIRPORT ?auto_1055 ) ( not ( = ?auto_1055 ?auto_1053 ) ) ( AIRPORT ?auto_1057 ) ( AIRPLANE-AT ?auto_1046 ?auto_1057 ) ( not ( = ?auto_1057 ?auto_1055 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_1046 ?auto_1057 ?auto_1055 )
      ( DELIVER-PKG ?auto_1042 ?auto_1043 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_758 - OBJ
      ?auto_759 - LOCATION
    )
    :vars
    (
      ?auto_763 - LOCATION
      ?auto_761 - CITY
      ?auto_762 - LOCATION
      ?auto_760 - CITY
      ?auto_766 - TRUCK
      ?auto_768 - LOCATION
      ?auto_769 - CITY
    )
    :precondition
    ( and ( IN-CITY ?auto_763 ?auto_761 ) ( IN-CITY ?auto_759 ?auto_761 ) ( not ( = ?auto_759 ?auto_763 ) ) ( OBJ-AT ?auto_758 ?auto_763 ) ( IN-CITY ?auto_762 ?auto_760 ) ( IN-CITY ?auto_763 ?auto_760 ) ( not ( = ?auto_763 ?auto_762 ) ) ( TRUCK-AT ?auto_766 ?auto_768 ) ( IN-CITY ?auto_768 ?auto_769 ) ( IN-CITY ?auto_762 ?auto_769 ) ( not ( = ?auto_762 ?auto_768 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_766 ?auto_768 ?auto_762 ?auto_769 )
      ( DELIVER-PKG ?auto_758 ?auto_759 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1074 - OBJ
      ?auto_1075 - LOCATION
    )
    :vars
    (
      ?auto_1081 - LOCATION
      ?auto_1076 - LOCATION
      ?auto_1086 - LOCATION
      ?auto_1078 - CITY
      ?auto_1077 - LOCATION
      ?auto_1082 - CITY
      ?auto_1083 - LOCATION
      ?auto_1079 - LOCATION
      ?auto_1085 - LOCATION
      ?auto_1080 - AIRPLANE
      ?auto_1084 - TRUCK
      ?auto_1090 - LOCATION
      ?auto_1091 - CITY
    )
    :precondition
    ( and ( AIRPORT ?auto_1081 ) ( AIRPORT ?auto_1075 ) ( not ( = ?auto_1081 ?auto_1075 ) ) ( AIRPORT ?auto_1076 ) ( not ( = ?auto_1076 ?auto_1081 ) ) ( IN-CITY ?auto_1086 ?auto_1078 ) ( IN-CITY ?auto_1081 ?auto_1078 ) ( not ( = ?auto_1081 ?auto_1086 ) ) ( OBJ-AT ?auto_1074 ?auto_1086 ) ( IN-CITY ?auto_1077 ?auto_1082 ) ( IN-CITY ?auto_1086 ?auto_1082 ) ( not ( = ?auto_1086 ?auto_1077 ) ) ( AIRPORT ?auto_1083 ) ( not ( = ?auto_1083 ?auto_1076 ) ) ( AIRPORT ?auto_1079 ) ( not ( = ?auto_1079 ?auto_1083 ) ) ( AIRPORT ?auto_1085 ) ( AIRPLANE-AT ?auto_1080 ?auto_1085 ) ( not ( = ?auto_1085 ?auto_1079 ) ) ( TRUCK-AT ?auto_1084 ?auto_1090 ) ( IN-CITY ?auto_1090 ?auto_1091 ) ( IN-CITY ?auto_1077 ?auto_1091 ) ( not ( = ?auto_1077 ?auto_1090 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_1084 ?auto_1090 ?auto_1077 ?auto_1091 )
      ( DELIVER-PKG ?auto_1074 ?auto_1075 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1110 - OBJ
      ?auto_1111 - LOCATION
    )
    :vars
    (
      ?auto_1126 - LOCATION
      ?auto_1116 - LOCATION
      ?auto_1115 - LOCATION
      ?auto_1119 - CITY
      ?auto_1122 - LOCATION
      ?auto_1125 - CITY
      ?auto_1124 - LOCATION
      ?auto_1114 - LOCATION
      ?auto_1123 - LOCATION
      ?auto_1113 - AIRPLANE
      ?auto_1117 - LOCATION
      ?auto_1112 - CITY
      ?auto_1118 - TRUCK
      ?auto_1128 - LOCATION
      ?auto_1129 - CITY
    )
    :precondition
    ( and ( AIRPORT ?auto_1126 ) ( AIRPORT ?auto_1111 ) ( not ( = ?auto_1126 ?auto_1111 ) ) ( AIRPORT ?auto_1116 ) ( not ( = ?auto_1116 ?auto_1126 ) ) ( IN-CITY ?auto_1115 ?auto_1119 ) ( IN-CITY ?auto_1126 ?auto_1119 ) ( not ( = ?auto_1126 ?auto_1115 ) ) ( OBJ-AT ?auto_1110 ?auto_1115 ) ( IN-CITY ?auto_1122 ?auto_1125 ) ( IN-CITY ?auto_1115 ?auto_1125 ) ( not ( = ?auto_1115 ?auto_1122 ) ) ( AIRPORT ?auto_1124 ) ( not ( = ?auto_1124 ?auto_1116 ) ) ( AIRPORT ?auto_1114 ) ( not ( = ?auto_1114 ?auto_1124 ) ) ( AIRPORT ?auto_1123 ) ( AIRPLANE-AT ?auto_1113 ?auto_1123 ) ( not ( = ?auto_1123 ?auto_1114 ) ) ( IN-CITY ?auto_1117 ?auto_1112 ) ( IN-CITY ?auto_1122 ?auto_1112 ) ( not ( = ?auto_1122 ?auto_1117 ) ) ( TRUCK-AT ?auto_1118 ?auto_1128 ) ( IN-CITY ?auto_1128 ?auto_1129 ) ( IN-CITY ?auto_1117 ?auto_1129 ) ( not ( = ?auto_1117 ?auto_1128 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_1118 ?auto_1128 ?auto_1117 ?auto_1129 )
      ( DELIVER-PKG ?auto_1110 ?auto_1111 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1169 - OBJ
      ?auto_1170 - LOCATION
    )
    :vars
    (
      ?auto_1171 - LOCATION
      ?auto_1176 - CITY
      ?auto_1172 - TRUCK
      ?auto_1174 - LOCATION
      ?auto_1173 - CITY
      ?auto_1179 - AIRPLANE
    )
    :precondition
    ( and ( IN-CITY ?auto_1171 ?auto_1176 ) ( IN-CITY ?auto_1170 ?auto_1176 ) ( not ( = ?auto_1170 ?auto_1171 ) ) ( TRUCK-AT ?auto_1172 ?auto_1174 ) ( IN-CITY ?auto_1174 ?auto_1173 ) ( IN-CITY ?auto_1171 ?auto_1173 ) ( not ( = ?auto_1171 ?auto_1174 ) ) ( IN-AIRPLANE ?auto_1169 ?auto_1179 ) ( AIRPLANE-AT ?auto_1179 ?auto_1171 ) )
    :subtasks
    ( ( DELIVER-PKG ?auto_1169 ?auto_1171 )
      ( DELIVER-PKG ?auto_1169 ?auto_1170 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1181 - OBJ
      ?auto_1182 - LOCATION
    )
    :vars
    (
      ?auto_1188 - LOCATION
      ?auto_1187 - CITY
      ?auto_1190 - TRUCK
      ?auto_1189 - LOCATION
      ?auto_1186 - CITY
      ?auto_1184 - AIRPLANE
      ?auto_1192 - LOCATION
    )
    :precondition
    ( and ( IN-CITY ?auto_1188 ?auto_1187 ) ( IN-CITY ?auto_1182 ?auto_1187 ) ( not ( = ?auto_1182 ?auto_1188 ) ) ( TRUCK-AT ?auto_1190 ?auto_1189 ) ( IN-CITY ?auto_1189 ?auto_1186 ) ( IN-CITY ?auto_1188 ?auto_1186 ) ( not ( = ?auto_1188 ?auto_1189 ) ) ( IN-AIRPLANE ?auto_1181 ?auto_1184 ) ( AIRPORT ?auto_1192 ) ( AIRPORT ?auto_1188 ) ( AIRPLANE-AT ?auto_1184 ?auto_1192 ) ( not ( = ?auto_1192 ?auto_1188 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_1184 ?auto_1192 ?auto_1188 )
      ( DELIVER-PKG ?auto_1181 ?auto_1182 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1194 - OBJ
      ?auto_1195 - LOCATION
    )
    :vars
    (
      ?auto_1196 - LOCATION
      ?auto_1197 - CITY
      ?auto_1198 - TRUCK
      ?auto_1201 - LOCATION
      ?auto_1204 - CITY
      ?auto_1200 - LOCATION
      ?auto_1203 - AIRPLANE
      ?auto_1205 - LOCATION
    )
    :precondition
    ( and ( IN-CITY ?auto_1196 ?auto_1197 ) ( IN-CITY ?auto_1195 ?auto_1197 ) ( not ( = ?auto_1195 ?auto_1196 ) ) ( TRUCK-AT ?auto_1198 ?auto_1201 ) ( IN-CITY ?auto_1201 ?auto_1204 ) ( IN-CITY ?auto_1196 ?auto_1204 ) ( not ( = ?auto_1196 ?auto_1201 ) ) ( AIRPORT ?auto_1200 ) ( AIRPORT ?auto_1196 ) ( AIRPLANE-AT ?auto_1203 ?auto_1200 ) ( not ( = ?auto_1200 ?auto_1196 ) ) ( OBJ-AT ?auto_1194 ?auto_1205 ) ( AIRPLANE-AT ?auto_1203 ?auto_1205 ) )
    :subtasks
    ( ( !LOAD-AIRPLANE ?auto_1194 ?auto_1203 ?auto_1205 )
      ( DELIVER-PKG ?auto_1194 ?auto_1195 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_3510 - OBJ
      ?auto_3511 - LOCATION
    )
    :vars
    (
      ?auto_3522 - LOCATION
      ?auto_3520 - CITY
      ?auto_3514 - TRUCK
      ?auto_3516 - LOCATION
      ?auto_3517 - CITY
      ?auto_3515 - LOCATION
      ?auto_3521 - LOCATION
      ?auto_3512 - LOCATION
      ?auto_3524 - LOCATION
      ?auto_3513 - AIRPLANE
    )
    :precondition
    ( and ( IN-CITY ?auto_3522 ?auto_3520 ) ( IN-CITY ?auto_3511 ?auto_3520 ) ( not ( = ?auto_3511 ?auto_3522 ) ) ( TRUCK-AT ?auto_3514 ?auto_3516 ) ( IN-CITY ?auto_3516 ?auto_3517 ) ( IN-CITY ?auto_3522 ?auto_3517 ) ( not ( = ?auto_3522 ?auto_3516 ) ) ( AIRPORT ?auto_3515 ) ( AIRPORT ?auto_3522 ) ( not ( = ?auto_3515 ?auto_3522 ) ) ( OBJ-AT ?auto_3510 ?auto_3515 ) ( AIRPORT ?auto_3521 ) ( not ( = ?auto_3521 ?auto_3515 ) ) ( AIRPORT ?auto_3512 ) ( not ( = ?auto_3512 ?auto_3521 ) ) ( AIRPORT ?auto_3524 ) ( AIRPLANE-AT ?auto_3513 ?auto_3524 ) ( not ( = ?auto_3524 ?auto_3512 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_3513 ?auto_3524 ?auto_3512 )
      ( DELIVER-PKG ?auto_3510 ?auto_3511 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1223 - OBJ
      ?auto_1224 - LOCATION
    )
    :vars
    (
      ?auto_1233 - LOCATION
      ?auto_1231 - CITY
      ?auto_1232 - TRUCK
      ?auto_1226 - LOCATION
      ?auto_1234 - CITY
      ?auto_1228 - LOCATION
      ?auto_1225 - LOCATION
      ?auto_1227 - AIRPLANE
      ?auto_1236 - TRUCK
    )
    :precondition
    ( and ( IN-CITY ?auto_1233 ?auto_1231 ) ( IN-CITY ?auto_1224 ?auto_1231 ) ( not ( = ?auto_1224 ?auto_1233 ) ) ( TRUCK-AT ?auto_1232 ?auto_1226 ) ( IN-CITY ?auto_1226 ?auto_1234 ) ( IN-CITY ?auto_1233 ?auto_1234 ) ( not ( = ?auto_1233 ?auto_1226 ) ) ( AIRPORT ?auto_1228 ) ( AIRPORT ?auto_1233 ) ( not ( = ?auto_1228 ?auto_1233 ) ) ( AIRPORT ?auto_1225 ) ( AIRPLANE-AT ?auto_1227 ?auto_1225 ) ( not ( = ?auto_1225 ?auto_1228 ) ) ( TRUCK-AT ?auto_1236 ?auto_1228 ) ( IN-TRUCK ?auto_1223 ?auto_1236 ) )
    :subtasks
    ( ( DELIVER-PKG ?auto_1223 ?auto_1228 )
      ( DELIVER-PKG ?auto_1223 ?auto_1224 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1238 - OBJ
      ?auto_1239 - LOCATION
    )
    :vars
    (
      ?auto_1245 - LOCATION
      ?auto_1246 - CITY
      ?auto_1244 - TRUCK
      ?auto_1240 - LOCATION
      ?auto_1241 - CITY
      ?auto_1242 - LOCATION
      ?auto_1249 - LOCATION
      ?auto_1250 - AIRPLANE
      ?auto_1247 - TRUCK
      ?auto_1252 - LOCATION
      ?auto_1253 - CITY
    )
    :precondition
    ( and ( IN-CITY ?auto_1245 ?auto_1246 ) ( IN-CITY ?auto_1239 ?auto_1246 ) ( not ( = ?auto_1239 ?auto_1245 ) ) ( TRUCK-AT ?auto_1244 ?auto_1240 ) ( IN-CITY ?auto_1240 ?auto_1241 ) ( IN-CITY ?auto_1245 ?auto_1241 ) ( not ( = ?auto_1245 ?auto_1240 ) ) ( AIRPORT ?auto_1242 ) ( AIRPORT ?auto_1245 ) ( not ( = ?auto_1242 ?auto_1245 ) ) ( AIRPORT ?auto_1249 ) ( AIRPLANE-AT ?auto_1250 ?auto_1249 ) ( not ( = ?auto_1249 ?auto_1242 ) ) ( IN-TRUCK ?auto_1238 ?auto_1247 ) ( TRUCK-AT ?auto_1247 ?auto_1252 ) ( IN-CITY ?auto_1252 ?auto_1253 ) ( IN-CITY ?auto_1242 ?auto_1253 ) ( not ( = ?auto_1242 ?auto_1252 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_1247 ?auto_1252 ?auto_1242 ?auto_1253 )
      ( DELIVER-PKG ?auto_1238 ?auto_1239 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1255 - OBJ
      ?auto_1256 - LOCATION
    )
    :vars
    (
      ?auto_1264 - LOCATION
      ?auto_1257 - CITY
      ?auto_1261 - TRUCK
      ?auto_1258 - LOCATION
      ?auto_1259 - CITY
      ?auto_1260 - LOCATION
      ?auto_1266 - LOCATION
      ?auto_1267 - AIRPLANE
      ?auto_1265 - TRUCK
      ?auto_1268 - LOCATION
      ?auto_1269 - CITY
      ?auto_1271 - LOCATION
    )
    :precondition
    ( and ( IN-CITY ?auto_1264 ?auto_1257 ) ( IN-CITY ?auto_1256 ?auto_1257 ) ( not ( = ?auto_1256 ?auto_1264 ) ) ( TRUCK-AT ?auto_1261 ?auto_1258 ) ( IN-CITY ?auto_1258 ?auto_1259 ) ( IN-CITY ?auto_1264 ?auto_1259 ) ( not ( = ?auto_1264 ?auto_1258 ) ) ( AIRPORT ?auto_1260 ) ( AIRPORT ?auto_1264 ) ( not ( = ?auto_1260 ?auto_1264 ) ) ( AIRPORT ?auto_1266 ) ( AIRPLANE-AT ?auto_1267 ?auto_1266 ) ( not ( = ?auto_1266 ?auto_1260 ) ) ( TRUCK-AT ?auto_1265 ?auto_1268 ) ( IN-CITY ?auto_1268 ?auto_1269 ) ( IN-CITY ?auto_1260 ?auto_1269 ) ( not ( = ?auto_1260 ?auto_1268 ) ) ( TRUCK-AT ?auto_1265 ?auto_1271 ) ( OBJ-AT ?auto_1255 ?auto_1271 ) )
    :subtasks
    ( ( !LOAD-TRUCK ?auto_1255 ?auto_1265 ?auto_1271 )
      ( DELIVER-PKG ?auto_1255 ?auto_1256 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1273 - OBJ
      ?auto_1274 - LOCATION
    )
    :vars
    (
      ?auto_1275 - LOCATION
      ?auto_1284 - CITY
      ?auto_1281 - TRUCK
      ?auto_1285 - LOCATION
      ?auto_1286 - CITY
      ?auto_1282 - LOCATION
      ?auto_1277 - LOCATION
      ?auto_1276 - AIRPLANE
      ?auto_1283 - LOCATION
      ?auto_1279 - CITY
      ?auto_1280 - TRUCK
      ?auto_1290 - LOCATION
      ?auto_1291 - CITY
    )
    :precondition
    ( and ( IN-CITY ?auto_1275 ?auto_1284 ) ( IN-CITY ?auto_1274 ?auto_1284 ) ( not ( = ?auto_1274 ?auto_1275 ) ) ( TRUCK-AT ?auto_1281 ?auto_1285 ) ( IN-CITY ?auto_1285 ?auto_1286 ) ( IN-CITY ?auto_1275 ?auto_1286 ) ( not ( = ?auto_1275 ?auto_1285 ) ) ( AIRPORT ?auto_1282 ) ( AIRPORT ?auto_1275 ) ( not ( = ?auto_1282 ?auto_1275 ) ) ( AIRPORT ?auto_1277 ) ( AIRPLANE-AT ?auto_1276 ?auto_1277 ) ( not ( = ?auto_1277 ?auto_1282 ) ) ( IN-CITY ?auto_1283 ?auto_1279 ) ( IN-CITY ?auto_1282 ?auto_1279 ) ( not ( = ?auto_1282 ?auto_1283 ) ) ( OBJ-AT ?auto_1273 ?auto_1283 ) ( TRUCK-AT ?auto_1280 ?auto_1290 ) ( IN-CITY ?auto_1290 ?auto_1291 ) ( IN-CITY ?auto_1283 ?auto_1291 ) ( not ( = ?auto_1283 ?auto_1290 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_1280 ?auto_1290 ?auto_1283 ?auto_1291 )
      ( DELIVER-PKG ?auto_1273 ?auto_1274 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1514 - OBJ
      ?auto_1515 - LOCATION
    )
    :vars
    (
      ?auto_1528 - LOCATION
      ?auto_1523 - CITY
      ?auto_1530 - TRUCK
      ?auto_1524 - LOCATION
      ?auto_1525 - CITY
      ?auto_1531 - LOCATION
      ?auto_1521 - LOCATION
      ?auto_1519 - LOCATION
      ?auto_1526 - CITY
      ?auto_1520 - TRUCK
      ?auto_1522 - LOCATION
      ?auto_1518 - CITY
      ?auto_1516 - LOCATION
      ?auto_1532 - LOCATION
      ?auto_1534 - LOCATION
      ?auto_1517 - AIRPLANE
    )
    :precondition
    ( and ( IN-CITY ?auto_1528 ?auto_1523 ) ( IN-CITY ?auto_1515 ?auto_1523 ) ( not ( = ?auto_1515 ?auto_1528 ) ) ( TRUCK-AT ?auto_1530 ?auto_1524 ) ( IN-CITY ?auto_1524 ?auto_1525 ) ( IN-CITY ?auto_1528 ?auto_1525 ) ( not ( = ?auto_1528 ?auto_1524 ) ) ( AIRPORT ?auto_1531 ) ( AIRPORT ?auto_1528 ) ( not ( = ?auto_1531 ?auto_1528 ) ) ( AIRPORT ?auto_1521 ) ( not ( = ?auto_1521 ?auto_1531 ) ) ( IN-CITY ?auto_1519 ?auto_1526 ) ( IN-CITY ?auto_1531 ?auto_1526 ) ( not ( = ?auto_1531 ?auto_1519 ) ) ( OBJ-AT ?auto_1514 ?auto_1519 ) ( TRUCK-AT ?auto_1520 ?auto_1522 ) ( IN-CITY ?auto_1522 ?auto_1518 ) ( IN-CITY ?auto_1519 ?auto_1518 ) ( not ( = ?auto_1519 ?auto_1522 ) ) ( AIRPORT ?auto_1516 ) ( not ( = ?auto_1516 ?auto_1521 ) ) ( AIRPORT ?auto_1532 ) ( not ( = ?auto_1532 ?auto_1516 ) ) ( AIRPORT ?auto_1534 ) ( AIRPLANE-AT ?auto_1517 ?auto_1534 ) ( not ( = ?auto_1534 ?auto_1532 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_1517 ?auto_1534 ?auto_1532 )
      ( DELIVER-PKG ?auto_1514 ?auto_1515 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1474 - OBJ
      ?auto_1475 - LOCATION
    )
    :vars
    (
      ?auto_1479 - LOCATION
      ?auto_1482 - CITY
      ?auto_1483 - TRUCK
      ?auto_1486 - LOCATION
      ?auto_1480 - CITY
      ?auto_1481 - LOCATION
      ?auto_1476 - LOCATION
      ?auto_1477 - LOCATION
      ?auto_1478 - CITY
      ?auto_1488 - TRUCK
      ?auto_1487 - LOCATION
      ?auto_1485 - CITY
      ?auto_1491 - LOCATION
      ?auto_1493 - LOCATION
      ?auto_1489 - AIRPLANE
    )
    :precondition
    ( and ( IN-CITY ?auto_1479 ?auto_1482 ) ( IN-CITY ?auto_1475 ?auto_1482 ) ( not ( = ?auto_1475 ?auto_1479 ) ) ( TRUCK-AT ?auto_1483 ?auto_1486 ) ( IN-CITY ?auto_1486 ?auto_1480 ) ( IN-CITY ?auto_1479 ?auto_1480 ) ( not ( = ?auto_1479 ?auto_1486 ) ) ( AIRPORT ?auto_1481 ) ( AIRPORT ?auto_1479 ) ( not ( = ?auto_1481 ?auto_1479 ) ) ( AIRPORT ?auto_1476 ) ( not ( = ?auto_1476 ?auto_1481 ) ) ( IN-CITY ?auto_1477 ?auto_1478 ) ( IN-CITY ?auto_1481 ?auto_1478 ) ( not ( = ?auto_1481 ?auto_1477 ) ) ( OBJ-AT ?auto_1474 ?auto_1477 ) ( TRUCK-AT ?auto_1488 ?auto_1487 ) ( IN-CITY ?auto_1487 ?auto_1485 ) ( IN-CITY ?auto_1477 ?auto_1485 ) ( not ( = ?auto_1477 ?auto_1487 ) ) ( AIRPORT ?auto_1491 ) ( not ( = ?auto_1491 ?auto_1476 ) ) ( AIRPORT ?auto_1493 ) ( AIRPLANE-AT ?auto_1489 ?auto_1493 ) ( not ( = ?auto_1493 ?auto_1491 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_1489 ?auto_1493 ?auto_1491 )
      ( DELIVER-PKG ?auto_1474 ?auto_1475 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1556 - OBJ
      ?auto_1557 - LOCATION
    )
    :vars
    (
      ?auto_1565 - LOCATION
      ?auto_1560 - CITY
      ?auto_1569 - TRUCK
      ?auto_1562 - LOCATION
      ?auto_1564 - CITY
      ?auto_1568 - LOCATION
      ?auto_1558 - LOCATION
      ?auto_1574 - LOCATION
      ?auto_1575 - CITY
      ?auto_1563 - LOCATION
      ?auto_1572 - CITY
      ?auto_1567 - LOCATION
      ?auto_1566 - LOCATION
      ?auto_1559 - LOCATION
      ?auto_1561 - AIRPLANE
      ?auto_1570 - TRUCK
      ?auto_1577 - LOCATION
      ?auto_1578 - CITY
    )
    :precondition
    ( and ( IN-CITY ?auto_1565 ?auto_1560 ) ( IN-CITY ?auto_1557 ?auto_1560 ) ( not ( = ?auto_1557 ?auto_1565 ) ) ( TRUCK-AT ?auto_1569 ?auto_1562 ) ( IN-CITY ?auto_1562 ?auto_1564 ) ( IN-CITY ?auto_1565 ?auto_1564 ) ( not ( = ?auto_1565 ?auto_1562 ) ) ( AIRPORT ?auto_1568 ) ( AIRPORT ?auto_1565 ) ( not ( = ?auto_1568 ?auto_1565 ) ) ( AIRPORT ?auto_1558 ) ( not ( = ?auto_1558 ?auto_1568 ) ) ( IN-CITY ?auto_1574 ?auto_1575 ) ( IN-CITY ?auto_1568 ?auto_1575 ) ( not ( = ?auto_1568 ?auto_1574 ) ) ( OBJ-AT ?auto_1556 ?auto_1574 ) ( IN-CITY ?auto_1563 ?auto_1572 ) ( IN-CITY ?auto_1574 ?auto_1572 ) ( not ( = ?auto_1574 ?auto_1563 ) ) ( AIRPORT ?auto_1567 ) ( not ( = ?auto_1567 ?auto_1558 ) ) ( AIRPORT ?auto_1566 ) ( not ( = ?auto_1566 ?auto_1567 ) ) ( AIRPORT ?auto_1559 ) ( AIRPLANE-AT ?auto_1561 ?auto_1559 ) ( not ( = ?auto_1559 ?auto_1566 ) ) ( TRUCK-AT ?auto_1570 ?auto_1577 ) ( IN-CITY ?auto_1577 ?auto_1578 ) ( IN-CITY ?auto_1563 ?auto_1578 ) ( not ( = ?auto_1563 ?auto_1577 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_1570 ?auto_1577 ?auto_1563 ?auto_1578 )
      ( DELIVER-PKG ?auto_1556 ?auto_1557 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1602 - OBJ
      ?auto_1603 - LOCATION
    )
    :vars
    (
      ?auto_1613 - LOCATION
      ?auto_1618 - CITY
      ?auto_1609 - TRUCK
      ?auto_1621 - LOCATION
      ?auto_1620 - CITY
      ?auto_1605 - LOCATION
      ?auto_1608 - LOCATION
      ?auto_1617 - LOCATION
      ?auto_1619 - CITY
      ?auto_1607 - LOCATION
      ?auto_1616 - CITY
      ?auto_1615 - LOCATION
      ?auto_1614 - LOCATION
      ?auto_1611 - LOCATION
      ?auto_1606 - AIRPLANE
      ?auto_1623 - LOCATION
      ?auto_1622 - CITY
      ?auto_1604 - TRUCK
      ?auto_1625 - LOCATION
      ?auto_1626 - CITY
    )
    :precondition
    ( and ( IN-CITY ?auto_1613 ?auto_1618 ) ( IN-CITY ?auto_1603 ?auto_1618 ) ( not ( = ?auto_1603 ?auto_1613 ) ) ( TRUCK-AT ?auto_1609 ?auto_1621 ) ( IN-CITY ?auto_1621 ?auto_1620 ) ( IN-CITY ?auto_1613 ?auto_1620 ) ( not ( = ?auto_1613 ?auto_1621 ) ) ( AIRPORT ?auto_1605 ) ( AIRPORT ?auto_1613 ) ( not ( = ?auto_1605 ?auto_1613 ) ) ( AIRPORT ?auto_1608 ) ( not ( = ?auto_1608 ?auto_1605 ) ) ( IN-CITY ?auto_1617 ?auto_1619 ) ( IN-CITY ?auto_1605 ?auto_1619 ) ( not ( = ?auto_1605 ?auto_1617 ) ) ( OBJ-AT ?auto_1602 ?auto_1617 ) ( IN-CITY ?auto_1607 ?auto_1616 ) ( IN-CITY ?auto_1617 ?auto_1616 ) ( not ( = ?auto_1617 ?auto_1607 ) ) ( AIRPORT ?auto_1615 ) ( not ( = ?auto_1615 ?auto_1608 ) ) ( AIRPORT ?auto_1614 ) ( not ( = ?auto_1614 ?auto_1615 ) ) ( AIRPORT ?auto_1611 ) ( AIRPLANE-AT ?auto_1606 ?auto_1611 ) ( not ( = ?auto_1611 ?auto_1614 ) ) ( IN-CITY ?auto_1623 ?auto_1622 ) ( IN-CITY ?auto_1607 ?auto_1622 ) ( not ( = ?auto_1607 ?auto_1623 ) ) ( TRUCK-AT ?auto_1604 ?auto_1625 ) ( IN-CITY ?auto_1625 ?auto_1626 ) ( IN-CITY ?auto_1623 ?auto_1626 ) ( not ( = ?auto_1623 ?auto_1625 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_1604 ?auto_1625 ?auto_1623 ?auto_1626 )
      ( DELIVER-PKG ?auto_1602 ?auto_1603 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_1887 - OBJ
      ?auto_1888 - LOCATION
    )
    :vars
    (
      ?auto_1891 - LOCATION
      ?auto_1889 - LOCATION
      ?auto_1895 - LOCATION
      ?auto_1892 - LOCATION
      ?auto_1896 - LOCATION
      ?auto_1897 - LOCATION
      ?auto_1899 - LOCATION
      ?auto_1893 - AIRPLANE
    )
    :precondition
    ( and ( AIRPORT ?auto_1891 ) ( AIRPORT ?auto_1888 ) ( not ( = ?auto_1891 ?auto_1888 ) ) ( OBJ-AT ?auto_1887 ?auto_1891 ) ( AIRPORT ?auto_1889 ) ( not ( = ?auto_1889 ?auto_1891 ) ) ( AIRPORT ?auto_1895 ) ( not ( = ?auto_1895 ?auto_1889 ) ) ( AIRPORT ?auto_1892 ) ( not ( = ?auto_1892 ?auto_1895 ) ) ( AIRPORT ?auto_1896 ) ( not ( = ?auto_1896 ?auto_1892 ) ) ( AIRPORT ?auto_1897 ) ( not ( = ?auto_1897 ?auto_1896 ) ) ( AIRPORT ?auto_1899 ) ( AIRPLANE-AT ?auto_1893 ?auto_1899 ) ( not ( = ?auto_1899 ?auto_1897 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_1893 ?auto_1899 ?auto_1897 )
      ( DELIVER-PKG ?auto_1887 ?auto_1888 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_2255 - OBJ
      ?auto_2256 - LOCATION
    )
    :vars
    (
      ?auto_2261 - TRUCK
      ?auto_2263 - LOCATION
      ?auto_2258 - CITY
      ?auto_2264 - LOCATION
      ?auto_2262 - LOCATION
      ?auto_2259 - LOCATION
      ?auto_2267 - LOCATION
      ?auto_2265 - AIRPLANE
    )
    :precondition
    ( and ( TRUCK-AT ?auto_2261 ?auto_2263 ) ( IN-CITY ?auto_2263 ?auto_2258 ) ( IN-CITY ?auto_2256 ?auto_2258 ) ( not ( = ?auto_2256 ?auto_2263 ) ) ( TRUCK-AT ?auto_2261 ?auto_2264 ) ( AIRPORT ?auto_2262 ) ( AIRPORT ?auto_2264 ) ( not ( = ?auto_2262 ?auto_2264 ) ) ( OBJ-AT ?auto_2255 ?auto_2262 ) ( AIRPORT ?auto_2259 ) ( not ( = ?auto_2259 ?auto_2262 ) ) ( AIRPORT ?auto_2267 ) ( AIRPLANE-AT ?auto_2265 ?auto_2267 ) ( not ( = ?auto_2267 ?auto_2259 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_2265 ?auto_2267 ?auto_2259 )
      ( DELIVER-PKG ?auto_2255 ?auto_2256 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_2945 - OBJ
      ?auto_2946 - LOCATION
    )
    :vars
    (
      ?auto_2955 - TRUCK
      ?auto_2950 - LOCATION
      ?auto_2962 - CITY
      ?auto_2953 - LOCATION
      ?auto_2951 - LOCATION
      ?auto_2958 - LOCATION
      ?auto_2954 - LOCATION
      ?auto_2961 - CITY
      ?auto_2956 - TRUCK
      ?auto_2948 - LOCATION
      ?auto_2947 - CITY
      ?auto_2952 - LOCATION
      ?auto_2959 - LOCATION
      ?auto_2964 - LOCATION
      ?auto_2949 - AIRPLANE
    )
    :precondition
    ( and ( TRUCK-AT ?auto_2955 ?auto_2950 ) ( IN-CITY ?auto_2950 ?auto_2962 ) ( IN-CITY ?auto_2946 ?auto_2962 ) ( not ( = ?auto_2946 ?auto_2950 ) ) ( TRUCK-AT ?auto_2955 ?auto_2953 ) ( AIRPORT ?auto_2951 ) ( AIRPORT ?auto_2953 ) ( not ( = ?auto_2951 ?auto_2953 ) ) ( AIRPORT ?auto_2958 ) ( not ( = ?auto_2958 ?auto_2951 ) ) ( IN-CITY ?auto_2954 ?auto_2961 ) ( IN-CITY ?auto_2951 ?auto_2961 ) ( not ( = ?auto_2951 ?auto_2954 ) ) ( OBJ-AT ?auto_2945 ?auto_2954 ) ( TRUCK-AT ?auto_2956 ?auto_2948 ) ( IN-CITY ?auto_2948 ?auto_2947 ) ( IN-CITY ?auto_2954 ?auto_2947 ) ( not ( = ?auto_2954 ?auto_2948 ) ) ( AIRPORT ?auto_2952 ) ( not ( = ?auto_2952 ?auto_2958 ) ) ( AIRPORT ?auto_2959 ) ( not ( = ?auto_2959 ?auto_2952 ) ) ( AIRPORT ?auto_2964 ) ( AIRPLANE-AT ?auto_2949 ?auto_2964 ) ( not ( = ?auto_2964 ?auto_2959 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_2949 ?auto_2964 ?auto_2959 )
      ( DELIVER-PKG ?auto_2945 ?auto_2946 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_2985 - OBJ
      ?auto_2986 - LOCATION
    )
    :vars
    (
      ?auto_2996 - TRUCK
      ?auto_2989 - LOCATION
      ?auto_2987 - CITY
      ?auto_2988 - LOCATION
      ?auto_3001 - LOCATION
      ?auto_2992 - LOCATION
      ?auto_2990 - LOCATION
      ?auto_2994 - CITY
      ?auto_2995 - TRUCK
      ?auto_3000 - LOCATION
      ?auto_2998 - CITY
      ?auto_2991 - LOCATION
      ?auto_2993 - LOCATION
      ?auto_3003 - LOCATION
      ?auto_3005 - LOCATION
      ?auto_2999 - AIRPLANE
    )
    :precondition
    ( and ( TRUCK-AT ?auto_2996 ?auto_2989 ) ( IN-CITY ?auto_2989 ?auto_2987 ) ( IN-CITY ?auto_2986 ?auto_2987 ) ( not ( = ?auto_2986 ?auto_2989 ) ) ( TRUCK-AT ?auto_2996 ?auto_2988 ) ( AIRPORT ?auto_3001 ) ( AIRPORT ?auto_2988 ) ( not ( = ?auto_3001 ?auto_2988 ) ) ( AIRPORT ?auto_2992 ) ( not ( = ?auto_2992 ?auto_3001 ) ) ( IN-CITY ?auto_2990 ?auto_2994 ) ( IN-CITY ?auto_3001 ?auto_2994 ) ( not ( = ?auto_3001 ?auto_2990 ) ) ( OBJ-AT ?auto_2985 ?auto_2990 ) ( TRUCK-AT ?auto_2995 ?auto_3000 ) ( IN-CITY ?auto_3000 ?auto_2998 ) ( IN-CITY ?auto_2990 ?auto_2998 ) ( not ( = ?auto_2990 ?auto_3000 ) ) ( AIRPORT ?auto_2991 ) ( not ( = ?auto_2991 ?auto_2992 ) ) ( AIRPORT ?auto_2993 ) ( not ( = ?auto_2993 ?auto_2991 ) ) ( AIRPORT ?auto_3003 ) ( not ( = ?auto_3003 ?auto_2993 ) ) ( AIRPORT ?auto_3005 ) ( AIRPLANE-AT ?auto_2999 ?auto_3005 ) ( not ( = ?auto_3005 ?auto_3003 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_2999 ?auto_3005 ?auto_3003 )
      ( DELIVER-PKG ?auto_2985 ?auto_2986 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_4031 - OBJ
      ?auto_4032 - LOCATION
    )
    :vars
    (
      ?auto_4039 - LOCATION
      ?auto_4042 - CITY
      ?auto_4044 - TRUCK
      ?auto_4034 - LOCATION
      ?auto_4040 - CITY
      ?auto_4037 - LOCATION
      ?auto_4041 - LOCATION
      ?auto_4036 - LOCATION
      ?auto_4038 - LOCATION
      ?auto_4046 - LOCATION
      ?auto_4043 - AIRPLANE
    )
    :precondition
    ( and ( IN-CITY ?auto_4039 ?auto_4042 ) ( IN-CITY ?auto_4032 ?auto_4042 ) ( not ( = ?auto_4032 ?auto_4039 ) ) ( TRUCK-AT ?auto_4044 ?auto_4034 ) ( IN-CITY ?auto_4034 ?auto_4040 ) ( IN-CITY ?auto_4039 ?auto_4040 ) ( not ( = ?auto_4039 ?auto_4034 ) ) ( AIRPORT ?auto_4037 ) ( AIRPORT ?auto_4039 ) ( not ( = ?auto_4037 ?auto_4039 ) ) ( OBJ-AT ?auto_4031 ?auto_4037 ) ( AIRPORT ?auto_4041 ) ( not ( = ?auto_4041 ?auto_4037 ) ) ( AIRPORT ?auto_4036 ) ( not ( = ?auto_4036 ?auto_4041 ) ) ( AIRPORT ?auto_4038 ) ( not ( = ?auto_4038 ?auto_4036 ) ) ( AIRPORT ?auto_4046 ) ( AIRPLANE-AT ?auto_4043 ?auto_4046 ) ( not ( = ?auto_4046 ?auto_4038 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_4043 ?auto_4046 ?auto_4038 )
      ( DELIVER-PKG ?auto_4031 ?auto_4032 ) )
  )

)

