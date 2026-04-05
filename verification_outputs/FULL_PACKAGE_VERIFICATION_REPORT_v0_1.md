# Full package verification report

## package_doctor.py
```json
{
  "doctor_version": "0.5.0",
  "status": "PASS",
  "total_checks": 111,
  "passed_checks": 111,
  "failed_checks": 0,
  "issues": []
}
```

## route1_launch_gate.py
```text
{
  "doctor_version": "0.5.0",
  "status": "PASS",
  "total_checks": 111,
  "passed_checks": 111,
  "failed_checks": 0,
  "issues": []
}

LAUNCH GATE: PASS
Route 1 current pilot package is present, verified, and research grounding is in passing state.
```

## prehuman suite
```json
{
  "version": "0.1.0",
  "status": "PASS",
  "runs": [
    {
      "script": "validate_evidence_tables.py",
      "returncode": 0,
      "stdout": "{\n  \"status\": \"PASS\",\n  \"issues\": []\n}\n"
    },
    {
      "script": "validate_datasets_manifest.py",
      "returncode": 0,
      "stdout": "{\n  \"status\": \"PASS\",\n  \"issues\": []\n}\n"
    }
  ]
}
```

## integrity verification
```json
{
  "manifest_version": "0.1.0",
  "verified_files": 62,
  "missing": [],
  "mismatches": [],
  "status": "PASS",
  "results": [
    {
      "path": "../governance/AUTHORITATIVE_INDEX_v0_1.md",
      "ok": true,
      "sha256": "08d66ee3926d211687cd8ca0c3e6650e0075936c56a46317456dfb57e64bb637"
    },
    {
      "path": "../governance/AUTHORITATIVE_SOURCES_v0_2.json",
      "ok": true,
      "sha256": "f01a5892fb1708c93cd6dee3ceb293f0553fe79ff70c63e5e8795657daf22748"
    },
    {
      "path": "docs/ops/CORRECTION_CYCLE_PROTOCOL_v0_1.md",
      "ok": true,
      "sha256": "eb260b10d447b5cf5cd14a20596c6b1699ca9d4ee1297fbbffa7a5cfa6eadedf"
    },
    {
      "path": "docs/frontdoor/CURRENT_OPERATOR_START_HERE_v0_1.md",
      "ok": true,
      "sha256": "3082c84b6e00f618c4b1d7cda4430902bf880653b58668ec43fc868a43d1177c"
    },
    {
      "path": "docs/frontdoor/HANDOFF_GUIDE_v0_1.md",
      "ok": true,
      "sha256": "1009b3b96adecf0e0c7d1fbb346a533a2b84a058242f42d3c29cda3f145fb9af"
    },
    {
      "path": "docs/ops/NEXT_STEP_PREP_route1_pilot_ops_v0_1_1.md",
      "ok": true,
      "sha256": "e4e4c158038f8fc5a16496a8e7aff674743821c3571716d1fb5521653a391702"
    },
    {
      "path": "docs/ops/PACKAGE_ENFORCEMENT_LAYER_v0_1.md",
      "ok": true,
      "sha256": "12680aaf33738ae546806c55dc64f10fc7c11488045244e7960f7ca700c00397"
    },
    {
      "path": "../governance/PACKAGE_STATE_SUMMARY_v0_1.json",
      "ok": true,
      "sha256": "ad118876c481b5cb211c2ad54d1bc17f6e5559a3ab300c9d5d488b2beb574018"
    },
    {
      "path": "README.md",
      "ok": true,
      "sha256": "e4225928b04635d7fc64d4cea10b3028bfaa1522a5f0a195e008cd24f685c2ea"
    },
    {
      "path": "docs/ops/allowed_values_response_form_route1_v0_2_anchored.md",
      "ok": true,
      "sha256": "d9fe5abd26b843e0ff674e391bc7f6a39e8fd7c66cdbe457c523f22dbe32010a"
    },
    {
      "path": "authoritative_guard.py",
      "ok": true,
      "sha256": "b05737ef3ee4e017e278973d2964168c94eabfa4ce7416a07fc9df569e49bb5d"
    },
    {
      "path": "docs/ops/baseline_protocol_memo_v0_2_redteamed.md",
      "ok": true,
      "sha256": "cac6e2d55784b89155502c609d0d1f3d787aaab346a084618eec49ccb22a313f"
    },
    {
      "path": "core/route1/correction_pairs.jsonl",
      "ok": true,
      "sha256": "6423b5c9182a6691586786a74e8deb2488ed72b332dd815bfebd9b3dcfa38955"
    },
    {
      "path": "cross_route_spec_v0_1/manifest.json",
      "ok": true,
      "sha256": "cc01c98c8653c5712019782d0e154d97218a5926953174d2eb143a7cdde3b546"
    },
    {
      "path": "core/route1/experiment_runner.py",
      "ok": true,
      "sha256": "4c440ffa4b65c2a33b6ee4bbee9d2b7fb2dd053130e8ae2eba2543697bf42200"
    },
    {
      "path": "core/route1/gold_invalid.jsonl",
      "ok": true,
      "sha256": "949ad81f7404c91fb562d95445b928ce78974d0c064d2590b161a053d22c54ab"
    },
    {
      "path": "core/route1/gold_valid.jsonl",
      "ok": true,
      "sha256": "caed7d67984a5cced10fb0c27748de69b643d119f8614a83fe4fb855ea7968a4"
    },
    {
      "path": "docs/ops/operator_checklist_route1_pilot_v0_1_1.md",
      "ok": true,
      "sha256": "4aa9a4428ff3c8f917f0f77222be49c15a8f9e8975ede773470737817de051cc"
    },
    {
      "path": "core/route1/parser.py",
      "ok": true,
      "sha256": "81ea50704183bb1f2c61d6bd679fb182d2b15a205fb7ae26d86069e86353e461"
    },
    {
      "path": "docs/ops/participant_instructions_route1_pilot_v0_2_anchored.md",
      "ok": true,
      "sha256": "ed9adaeed636d131d7f4d8bf7e5d7bc2a1a4b41a7f59ee3a9c8e41246b5bdf5b"
    },
    {
      "path": "core/route1/pilot_answer_key_route1_v0_4_alternate_aware.jsonl",
      "ok": true,
      "sha256": "e383045b69b4d0c36288b925725c1ea6159e923ab941ca324938fcddf794db22"
    },
    {
      "path": "core/route1/pilot_packet_route1_v0_3_final.jsonl",
      "ok": true,
      "sha256": "e7d1362fa5f7ed565ddfaf335c8b0f0a7641d4ddce3186ce14ce97256ae5a1f7"
    },
    {
      "path": "docs/ops/pilot_protocol_memo_v0_2_redteamed.md",
      "ok": true,
      "sha256": "d407142e17d61d7b9628db6499888902c6b594a1969c164c251a3cc70c7976c8"
    },
    {
      "path": "core/route1/pilot_response_template_route1_v0_2_anchored.json",
      "ok": true,
      "sha256": "4f2f85289f87ce5d834a94725469e53fdd3c653314b1e64cd378de3ea7ce2d7e"
    },
    {
      "path": "docs/ops/pilot_review_template_v0_2_redteamed.md",
      "ok": true,
      "sha256": "7d51350e9eb1fbe37854a6c1eb99a07eda2817afa7278a1b62357d07bfc7a6e1"
    },
    {
      "path": "research_grounding_v0_1/README.md",
      "ok": true,
      "sha256": "d6fc35c62f1c14bc8c996bd44b0978050119b19f9d48a5df300cbaca56fb8bde"
    },
    {
      "path": "research_grounding_v0_1/datasets_manifest_v0_1.json",
      "ok": true,
      "sha256": "8da0237a25d06d58c599dcf55b7c134fe33aefa7071efb5529ea9584b14c7fe4"
    },
    {
      "path": "research_grounding_v0_1/evidence_mapping_method_memo_v0_1.md",
      "ok": true,
      "sha256": "6c8a2fce7e8f981c02c2516d6ee6799b24002f045df353a2b93d904feb1c0a90"
    },
    {
      "path": "research_grounding_v0_1/field_registry_route1_v0_1.json",
      "ok": true,
      "sha256": "cb354920ffff2ed0ef7764f2f2c08f6b040a6df30b39a7ba0ff3f13d2c56a847"
    },
    {
      "path": "research_grounding_v0_1/field_registry_route2_v0_1.json",
      "ok": true,
      "sha256": "85a6f2cb600ebce8ba537446520601bc4a6863e753f1df8fcc6cdb9f9095dc68"
    },
    {
      "path": "research_grounding_v0_1/prehuman_validation_report_route1_v0_1.md",
      "ok": true,
      "sha256": "3754e0792e3c2b90fa9f6383c179c78bc99cd0ca945f96a07590339c21b3d9be"
    },
    {
      "path": "research_grounding_v0_1/prehuman_validation_report_route2_v0_1.md",
      "ok": true,
      "sha256": "43f83f324a2a602a22cfb65d9ac30a38a8241cb6094ffc9a76de5ba507fecef8"
    },
    {
      "path": "research_grounding_v0_1/prehuman_validation_rubric_v0_1.md",
      "ok": true,
      "sha256": "edbacc1d357137c773efeae51a70a6d0f35a6d5d7c48444353924b7c8a1bdc89"
    },
    {
      "path": "research_grounding_v0_1/prehuman_validation_summary_v0_1.json",
      "ok": true,
      "sha256": "530be0ec1b85f2fb5e1f0a5e30e07bf8518c839617fd572c20de8918d04ccb73"
    },
    {
      "path": "research_grounding_v0_1/reference_bibliography_v0_1.json",
      "ok": true,
      "sha256": "41b0184fc7386f9f9bc8be10eb848d7f911879efd07e8ad0f035cd90b1ca9f24"
    },
    {
      "path": "research_grounding_v0_1/reference_bibliography_v0_1.md",
      "ok": true,
      "sha256": "56108005918f2b51cfe179b17341a35a481b5b2e3fdf3dfb5bd9808032939f96"
    },
    {
      "path": "research_grounding_v0_1/route1_field_evidence_v0_1.csv",
      "ok": true,
      "sha256": "d3c07625a510b684e7911ec6219e9b5aa85f60e4172c8df97b812bc52f75e63d"
    },
    {
      "path": "research_grounding_v0_1/route1_field_evidence_v0_1.jsonl",
      "ok": true,
      "sha256": "b3eb1176e7f07c1923ed1c75d367350c3ce0126dd94f80f0d6f56c8082ab866f"
    },
    {
      "path": "research_grounding_v0_1/route1_scientific_grounding_memo_v0_1.md",
      "ok": true,
      "sha256": "8cce1eb458f97afc54045c32f88cd40d27226d507497c90900cc3ecac010092b"
    },
    {
      "path": "research_grounding_v0_1/route2_field_evidence_v0_1.csv",
      "ok": true,
      "sha256": "de63106b21f428eea250c57acd8a3c6b4f8940c6ba7cd1a7f7e529f884222853"
    },
    {
      "path": "research_grounding_v0_1/route2_field_evidence_v0_1.jsonl",
      "ok": true,
      "sha256": "b3725905c4d89d080e23131b07431701edcdb8d417af660905d7934b64516ee5"
    },
    {
      "path": "research_grounding_v0_1/route2_scientific_grounding_memo_v0_1.md",
      "ok": true,
      "sha256": "f6b8702e2971e7a9f3726eb59a01bcd6853be6360051d78b2bc09412b75f70e4"
    },
    {
      "path": "research_grounding_v0_1/scripts/generate_integrity_manifest.py",
      "ok": true,
      "sha256": "44368ea6d176c8f46e66c4a7864bca68a1aa9563b1fb30011b52a147553e333b"
    },
    {
      "path": "research_grounding_v0_1/scripts/run_prehuman_suite.py",
      "ok": true,
      "sha256": "5289d7071d37b4ec5e440ef361fa272634d96efa269de1d438b01db86a974d14"
    },
    {
      "path": "research_grounding_v0_1/scripts/synthesize_route2_stimuli.py",
      "ok": true,
      "sha256": "614d1233c5b4a9adcacec1c181cd5bd261803b92cf0bf991422fe8769c974227"
    },
    {
      "path": "research_grounding_v0_1/scripts/validate_datasets_manifest.py",
      "ok": true,
      "sha256": "552cc64b7f70324f1095a4db667955c788729c294b41799510f5144441b54537"
    },
    {
      "path": "research_grounding_v0_1/scripts/validate_evidence_tables.py",
      "ok": true,
      "sha256": "d47bf6466bf550cf60e92ef786d7bb1cbee7dfee032b4cc07bc3cc905dbdce29"
    },
    {
      "path": "research_grounding_v0_1/scripts/verify_integrity_manifest.py",
      "ok": true,
      "sha256": "9567fc710e68565867d66c4120220497b5e7a2ee8417cbc19bb07d4d64263ae5"
    },
    {
      "path": "research_grounding_v0_1/weight_priors_memo_v0_2.md",
      "ok": true,
      "sha256": "698312a17c41c4aaa298a3861c3697c4c60f1c03b64e5f8e3ff132dddeffdaf3"
    },
    {
      "path": "docs/ops/route1_calibration_examples_v0_1.md",
      "ok": true,
      "sha256": "f7699171bcf242905442943452d56ca4fbca962e32ca2fb7f1b6830525d03301"
    },
    {
      "path": "docs/ops/route1_pilot_clarification_layer_v0_1.md",
      "ok": true,
      "sha256": "2ca4cca8bf0d4931d899df6c7df1f763a2610f91c304ffd56ef16de66151a3df"
    },
    {
      "path": "route2_visual_v0_1/README.md",
      "ok": true,
      "sha256": "9ad0014fc9e38e6b4e895d53b353befe3fdfc75800a7370f9408ed81c1753ed8"
    },
    {
      "path": "route2_visual_v0_1/correction_pairs.jsonl",
      "ok": true,
      "sha256": "a499ea5876782a85c221a3aef01e41d87e9107ea28a36fe35824f6dbfa7a21e7"
    },
    {
      "path": "route2_visual_v0_1/experiment_runner.py",
      "ok": true,
      "sha256": "aae4fb82eeb74e34e724e23bee19920099cf68071dbf9969b2231586ff3a371b"
    },
    {
      "path": "route2_visual_v0_1/gold_invalid.jsonl",
      "ok": true,
      "sha256": "0a43b406a887bc5f2ccda0dd32a63708a4919189348a628f9606a2c2a941d8bd"
    },
    {
      "path": "route2_visual_v0_1/gold_valid.jsonl",
      "ok": true,
      "sha256": "c0063e356735f65139d6f8b79ba5852cce956663034e32c18a493ec7ddff7dbc"
    },
    {
      "path": "route2_visual_v0_1/parser.py",
      "ok": true,
      "sha256": "ce91a01e183789ec87385c8d5ecdca15523b2613c6b39fae0ac190b39f8332d3"
    },
    {
      "path": "route2_visual_v0_1/scorer.py",
      "ok": true,
      "sha256": "aaba60751465e81d6215fe05b7bbbabc3ac25388bdd4473eea964932ff300232"
    },
    {
      "path": "core/route1/scorer.py",
      "ok": true,
      "sha256": "c84ef992eb76f0fd55d499f426bed5074dff152d638496807f83a88198ae05c5"
    },
    {
      "path": "core/route1/token_legend_route1_v0_1.md",
      "ok": true,
      "sha256": "9d64bda7e18aa2137d60525d46aa3323df1a909a610923a59b441afa20e2e0f8"
    },
    {
      "path": "tools/convert_route1_responses_to_predictions.py",
      "ok": true,
      "sha256": "b982b1a7848fc70c1609fa307a338cfd6c3a69fc1427e7349902839ec6ffa9e2"
    },
    {
      "path": "tools/run_route1_current_ops.py",
      "ok": true,
      "sha256": "2d653db0ab38aeb91821a8f777d717b78c9b944bed23f0b485094ca958bdce22"
    }
  ]
}
```
