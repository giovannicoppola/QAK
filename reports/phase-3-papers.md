# Phase 3: Paper Notes — Migration Report

- **Date:** 2026-04-16 12:54
- **Notes processed:** 722
- **Notes modified:** 722
- **Notes skipped:** 0
- **Errors:** 0

## Summary

Added `type: paper` YAML frontmatter to paper notes. Extracted citekey from filename, 
first author and year from citekey, diseases and genes from wiki-links and text patterns, 
study type by keyword inference, sample sizes from body text, and detected `#obs` blocks. 
All original body text preserved. AI-generated summaries (`OBSummary_AI`) deferred to Phase 9.

## YAML Properties Populated

| Property | Populated | Left Empty | Notes |
|----------|----------:|----------:|-------|
| type | 722/722 | 0 | always 'paper' |
| citekey | 722/722 | 0 | from filename |
| first_author | 722/722 | 0 | from citekey |
| year | 722/722 | 0 | from citekey |
| diseases | 316/722 | 406 | from links + text patterns |
| genes | 124/722 | 598 | from [[^GENE]] links |
| study_type | 216/722 | 506 | keyword inference |
| n_total | 82/722 | 640 | from body text |
| obs_source | 131/722 | 591 | 131 human, 591 empty (AI gen deferred) |
| title | 0/722 | 722 | needs bibliographic DB |
| journal | 0/722 | 722 | needs bibliographic DB |

## Changes by Note

| Note | Status | Changes | Warnings |
|------|--------|---------|----------|
| @AREDS2_Research_Group2012-cx.md | modified | +type: paper; +citekey: AREDS2_Research_Group2012-cx; +diseases: 1; +study_type: clinical-trial; +n_total: 1012 | — |
| @Abu-Hassan2014-zw.md | modified | +type: paper; +citekey: Abu-Hassan2014-zw | diseases empty; study_type not inferred |
| @Adadey2020-yd.md | modified | +type: paper; +citekey: Adadey2020-yd; +genes: 1; +study_type: review; +obs_source: human | diseases empty |
| @Adams2019-uu.md | modified | +type: paper; +citekey: Adams2019-uu; +diseases: 2 | study_type not inferred |
| @Adler2019-oq.md | modified | +type: paper; +citekey: Adler2019-oq | diseases empty; study_type not inferred |
| @Aisen2020-me.md | modified | +type: paper; +citekey: Aisen2020-me; +diseases: 1; +study_type: review | — |
| @Aisen2022-ni.md | modified | +type: paper; +citekey: Aisen2022-ni; +diseases: 1; +study_type: review; +obs_source: human | — |
| @Akbari2021-py.md | modified | +type: paper; +citekey: Akbari2021-py | diseases empty; study_type not inferred |
| @Akinc2019-su.md | modified | +type: paper; +citekey: Akinc2019-su | diseases empty; study_type not inferred |
| @Aksman2023-gq.md | modified | +type: paper; +citekey: Aksman2023-gq; +diseases: 1; +obs_source: human | study_type not inferred |
| @Albuquerque2009-ke.md | modified | +type: paper; +citekey: Albuquerque2009-ke | diseases empty; study_type not inferred |
| @Alden2021-fj.md | modified | +type: paper; +citekey: Alden2021-fj; +diseases: 1 | study_type not inferred |
| @Alsema2020-gm.md | modified | +type: paper; +citekey: Alsema2020-gm; +diseases: 1; +n_total: 10; +obs_source: human | study_type not inferred |
| @Altmann2020-ge.md | modified | +type: paper; +citekey: Altmann2020-ge; +diseases: 1 | study_type not inferred |
| @Altmann2024-zy.md | modified | +type: paper; +citekey: Altmann2024-zy; +diseases: 1; +study_type: gwas; +obs_source: human | — |
| @American Caesar, Douglas MacArthur.md | modified | +type: paper; +citekey: American Caesar, Douglas MacArthur | diseases empty; study_type not inferred |
| @Andres2010-ds.md | modified | +type: paper; +citekey: Andres2010-ds; +n_total: 19 | diseases empty; study_type not inferred |
| @Apte2021-tl.md | modified | +type: paper; +citekey: Apte2021-tl; +diseases: 1 | study_type not inferred |
| @Arboleda-Velasquez2019-lo.md | modified | +type: paper; +citekey: Arboleda-Velasquez2019-lo; +diseases: 2; +genes: 1 | study_type not inferred |
| @Arcondeguy2013-rf.md | modified | +type: paper; +citekey: Arcondeguy2013-rf | diseases empty; study_type not inferred |
| @Arnold2018-gq.md | modified | +type: paper; +citekey: Arnold2018-gq; +diseases: 1 | study_type not inferred |
| @Ashford2020-zc.md | modified | +type: paper; +citekey: Ashford2020-zc; +diseases: 1; +n_total: 533; +obs_source: human | study_type not inferred |
| @Ashton2020-qr.md | modified | +type: paper; +citekey: Ashton2020-qr | diseases empty; study_type not inferred |
| @Askew2015-cv.md | modified | +type: paper; +citekey: Askew2015-cv; +genes: 1; +study_type: functional | diseases empty |
| @Australia_and_New_Zealand_Multiple_Sclerosis_Genetics_Consortium_ANZgene2009-ro.md | modified | +type: paper; +citekey: Australia_and_New_Zealand_Multiple_Sclerosis_Genetics_Consortium_ANZgene2009-ro; +diseases: 1; +study_type: gwas | — |
| @Babaie2020-oo.md | modified | +type: paper; +citekey: Babaie2020-oo | diseases empty; study_type not inferred |
| @Bach Music in the Castle of Heaven.md | modified | +type: paper; +citekey: Bach Music in the Castle of Heaven; +study_type: review | diseases empty |
| @Bach by Schweitzer Volume 2.md | modified | +type: paper; +citekey: Bach by Schweitzer Volume 2; +n_total: 17 | diseases empty; study_type not inferred |
| @Bacioglu2016-if.md | modified | +type: paper; +citekey: Bacioglu2016-if; +study_type: functional | diseases empty |
| @Bahat2024-ra.md | modified | +type: paper; +citekey: Bahat2024-ra; +diseases: 1 | study_type not inferred |
| @Baird2020-ef.md | modified | +type: paper; +citekey: Baird2020-ef | diseases empty; study_type not inferred |
| @Baker-Nigh2016-dn.md | modified | +type: paper; +citekey: Baker-Nigh2016-dn | diseases empty; study_type not inferred |
| @Baldwin2019-ya.md | modified | +type: paper; +citekey: Baldwin2019-ya; +genes: 1 | diseases empty; study_type not inferred |
| @Balendra2018-gs.md | modified | +type: paper; +citekey: Balendra2018-gs; +diseases: 2; +study_type: functional | — |
| @Balendra2025-vl.md | modified | +type: paper; +citekey: Balendra2025-vl; +diseases: 2; +genes: 1; +study_type: functional | — |
| @Banh2021-bj.md | modified | +type: paper; +citekey: Banh2021-bj | diseases empty; study_type not inferred |
| @Bar-Or2020-ck.md | modified | +type: paper; +citekey: Bar-Or2020-ck; +diseases: 1; +study_type: review; +obs_source: human | — |
| @Bartels2020-hr.md | modified | +type: paper; +citekey: Bartels2020-hr; +diseases: 2; +genes: 1; +study_type: review; +obs_source: human | — |
| @Bateman2012-xx.md | modified | +type: paper; +citekey: Bateman2012-xx; +diseases: 1 | study_type not inferred |
| @Bates2015-ns.md | modified | +type: paper; +citekey: Bates2015-ns | diseases empty; study_type not inferred |
| @Becanovic2015-lj.md | modified | +type: paper; +citekey: Becanovic2015-lj | diseases empty; study_type not inferred |
| @Bellenguez2020-rg.md | modified | +type: paper; +citekey: Bellenguez2020-rg; +diseases: 2; +study_type: gwas; +n_total: 41270; +obs_source: human | — |
| @Belloy2019-ae.md | modified | +type: paper; +citekey: Belloy2019-ae; +diseases: 3; +genes: 1 | study_type not inferred |
| @Belloy2023-by.md | modified | +type: paper; +citekey: Belloy2023-by; +diseases: 1; +genes: 1; +study_type: exome; +obs_source: human | — |
| @Benatar2022-si.md | modified | +type: paper; +citekey: Benatar2022-si | diseases empty; study_type not inferred |
| @Bennet2007-jj.md | modified | +type: paper; +citekey: Bennet2007-jj; +study_type: review; +obs_source: human | diseases empty |
| @Benson2022-kl.md | modified | +type: paper; +citekey: Benson2022-kl | diseases empty; study_type not inferred |
| @Berwick2019-ts.md | modified | +type: paper; +citekey: Berwick2019-ts; +study_type: functional | diseases empty |
| @Bhatnagar2020-ld.md | modified | +type: paper; +citekey: Bhatnagar2020-ld | diseases empty; study_type not inferred |
| @Bhattacharyya2021-wk.md | modified | +type: paper; +citekey: Bhattacharyya2021-wk; +diseases: 1 | study_type not inferred |
| @Biessels2006-tw.md | modified | +type: paper; +citekey: Biessels2006-tw | diseases empty; study_type not inferred |
| @Bjornevik2022-he.md | modified | +type: paper; +citekey: Bjornevik2022-he; +diseases: 1 | study_type not inferred |
| @Blauwendraat2018-ux.md | modified | +type: paper; +citekey: Blauwendraat2018-ux | diseases empty; study_type not inferred |
| @Bloem2021-vt.md | modified | +type: paper; +citekey: Bloem2021-vt; +diseases: 1; +genes: 2 | study_type not inferred |
| @Bloodlands.md | modified | +type: paper; +citekey: Bloodlands | diseases empty; study_type not inferred |
| @Blum2016-tq.md | modified | +type: paper; +citekey: Blum2016-tq | diseases empty; study_type not inferred |
| @Bonnet2019-ah.md | modified | +type: paper; +citekey: Bonnet2019-ah; +diseases: 1 | study_type not inferred |
| @Born to Run.md | modified | +type: paper; +citekey: Born to Run | diseases empty; study_type not inferred |
| @Bosello2016-kb.md | modified | +type: paper; +citekey: Bosello2016-kb; +study_type: review | diseases empty |
| @Bourgade2016-hw.md | modified | +type: paper; +citekey: Bourgade2016-hw | diseases empty; study_type not inferred |
| @Bouzid2021-qj.md | modified | +type: paper; +citekey: Bouzid2021-qj; +diseases: 1 | study_type not inferred |
| @Bouzid2023-ci.md | modified | +type: paper; +citekey: Bouzid2023-ci; +study_type: review | diseases empty |
| @Boxer2019-xx.md | modified | +type: paper; +citekey: Boxer2019-xx; +diseases: 1; +study_type: clinical-trial | — |
| @Boyer2017-bu.md | modified | +type: paper; +citekey: Boyer2017-bu | diseases empty; study_type not inferred |
| @Braak1991-ml.md | modified | +type: paper; +citekey: Braak1991-ml; +diseases: 1 | study_type not inferred |
| @BradleyNeurology.md | modified | +type: paper; +citekey: BradleyNeurology | diseases empty; study_type not inferred |
| @Brainstorm.md | modified | +type: paper; +citekey: Brainstorm | diseases empty; study_type not inferred |
| @Brazel2019-gi.md | modified | +type: paper; +citekey: Brazel2019-gi; +genes: 1; +study_type: gwas; +obs_source: human | diseases empty |
| @Breath from Salt.md | modified | +type: paper; +citekey: Breath from Salt | diseases empty; study_type not inferred |
| @Broce2018-tk.md | modified | +type: paper; +citekey: Broce2018-tk; +diseases: 1; +study_type: gwas | — |
| @Bu2022-ax.md | modified | +type: paper; +citekey: Bu2022-ax; +genes: 1 | diseases empty; study_type not inferred |
| @Budd_Haeberlein2022-yb.md | modified | +type: paper; +citekey: Budd_Haeberlein2022-yb; +diseases: 1; +study_type: clinical-trial | — |
| @Buegler2020-lp.md | modified | +type: paper; +citekey: Buegler2020-lp; +n_total: 215 | diseases empty; study_type not inferred |
| @Buffault2020-ec.md | modified | +type: paper; +citekey: Buffault2020-ec; +study_type: review | diseases empty |
| @Burch2019-ok.md | modified | +type: paper; +citekey: Burch2019-ok | diseases empty; study_type not inferred |
| @Burdon2015-no.md | modified | +type: paper; +citekey: Burdon2015-no; +genes: 1; +study_type: gwas; +n_total: 336; +obs_source: human | diseases empty |
| @Burnham2020-il.md | modified | +type: paper; +citekey: Burnham2020-il; +diseases: 1; +obs_source: human | study_type not inferred |
| @Busche2020-bl.md | modified | +type: paper; +citekey: Busche2020-bl | diseases empty; study_type not inferred |
| @Busse2020-wi.md | modified | +type: paper; +citekey: Busse2020-wi; +study_type: review; +obs_source: human | diseases empty |
| @Bustos2020-zz.md | modified | +type: paper; +citekey: Bustos2020-zz; +diseases: 1; +study_type: exome | — |
| @Butovsky2018-no.md | modified | +type: paper; +citekey: Butovsky2018-no; +genes: 2; +study_type: review | diseases empty |
| @Campion2019-dw.md | modified | +type: paper; +citekey: Campion2019-dw; +diseases: 1; +genes: 1; +study_type: review; +n_total: 18850; +obs_source: human | — |
| @Cannon-Albright2019-ky.md | modified | +type: paper; +citekey: Cannon-Albright2019-ky | diseases empty; study_type not inferred |
| @Capellini2017-yd.md | modified | +type: paper; +citekey: Capellini2017-yd | diseases empty; study_type not inferred |
| @Carroll2011-pe.md | modified | +type: paper; +citekey: Carroll2011-pe; +diseases: 1; +genes: 1 | study_type not inferred |
| @Carvalho2019-ss.md | modified | +type: paper; +citekey: Carvalho2019-ss | diseases empty; study_type not inferred |
| @Cassa2017-pl.md | modified | +type: paper; +citekey: Cassa2017-pl; +study_type: exome | diseases empty |
| @Cassidy2012-lr.md | modified | +type: paper; +citekey: Cassidy2012-lr | diseases empty; study_type not inferred |
| @Chabriat2009-zh.md | modified | +type: paper; +citekey: Chabriat2009-zh; +diseases: 2; +genes: 1 | study_type not inferred |
| @Chan2017-gl.md | modified | +type: paper; +citekey: Chan2017-gl | diseases empty; study_type not inferred |
| @Chang2021-ji.md | modified | +type: paper; +citekey: Chang2021-ji | diseases empty; study_type not inferred |
| @Chasioti2019-nb.md | modified | +type: paper; +citekey: Chasioti2019-nb; +diseases: 1; +obs_source: human | study_type not inferred |
| @Chen2014-mb.md | modified | +type: paper; +citekey: Chen2014-mb; +genes: 1 | diseases empty; study_type not inferred |
| @Chen2021-cu.md | modified | +type: paper; +citekey: Chen2021-cu; +diseases: 1; +genes: 1; +study_type: exome; +obs_source: human | — |
| @Chen2021-ld.md | modified | +type: paper; +citekey: Chen2021-ld; +diseases: 1 | study_type not inferred |
| @Chen2022-df.md | modified | +type: paper; +citekey: Chen2022-df; +n_total: 15 | diseases empty; study_type not inferred |
| @Chhatwal2022-jd.md | modified | +type: paper; +citekey: Chhatwal2022-jd; +diseases: 1 | study_type not inferred |
| @Chia2021-ue.md | modified | +type: paper; +citekey: Chia2021-ue; +diseases: 1; +genes: 5; +study_type: gwas; +obs_source: human | — |
| @Chick1992-kj.md | modified | +type: paper; +citekey: Chick1992-kj | diseases empty; study_type not inferred |
| @Cho2020-qt.md | modified | +type: paper; +citekey: Cho2020-qt | diseases empty; study_type not inferred |
| @Choe2023-lt.md | modified | +type: paper; +citekey: Choe2023-lt; +obs_source: human | diseases empty; study_type not inferred |
| @Choy2020-my.md | modified | +type: paper; +citekey: Choy2020-my; +diseases: 2; +study_type: clinical-trial | — |
| @Cipriani2020-ka.md | modified | +type: paper; +citekey: Cipriani2020-ka; +diseases: 1 | study_type not inferred |
| @Coban-Akdemir2018-sm.md | modified | +type: paper; +citekey: Coban-Akdemir2018-sm; +genes: 1 | diseases empty; study_type not inferred |
| @Cochran2020-un.md | modified | +type: paper; +citekey: Cochran2020-un; +diseases: 2; +n_total: 1106; +obs_source: human | study_type not inferred |
| @Cole2020-me.md | modified | +type: paper; +citekey: Cole2020-me; +study_type: gwas; +n_total: 43565 | diseases empty |
| @Comi2020-rh.md | modified | +type: paper; +citekey: Comi2020-rh; +diseases: 1; +genes: 1 | study_type not inferred |
| @Compagnone2019-ap.md | modified | +type: paper; +citekey: Compagnone2019-ap | diseases empty; study_type not inferred |
| @Conroy2022-mh.md | modified | +type: paper; +citekey: Conroy2022-mh | diseases empty; study_type not inferred |
| @Corbett2018-wg.md | modified | +type: paper; +citekey: Corbett2018-wg | diseases empty; study_type not inferred |
| @Cornejo-Sanchez2023-bl.md | modified | +type: paper; +citekey: Cornejo-Sanchez2023-bl | diseases empty; study_type not inferred |
| @Cortese2019-dx.md | modified | +type: paper; +citekey: Cortese2019-dx | diseases empty; study_type not inferred |
| @Cortese2020-io.md | modified | +type: paper; +citekey: Cortese2020-io | diseases empty; study_type not inferred |
| @Costa2017-vp.md | modified | +type: paper; +citekey: Costa2017-vp; +genes: 1 | diseases empty; study_type not inferred |
| @Cotsapas2018-ui.md | modified | +type: paper; +citekey: Cotsapas2018-ui; +diseases: 4; +genes: 3; +study_type: gwas; +obs_source: human | — |
| @Coutinho2020-rl.md | modified | +type: paper; +citekey: Coutinho2020-rl; +genes: 1; +obs_source: human | diseases empty; study_type not inferred |
| @Craddock2013-ud.md | modified | +type: paper; +citekey: Craddock2013-ud | diseases empty; study_type not inferred |
| @Craft1998-qo.md | modified | +type: paper; +citekey: Craft1998-qo | diseases empty; study_type not inferred |
| @Crary2014-ws.md | modified | +type: paper; +citekey: Crary2014-ws | diseases empty; study_type not inferred |
| @Crime and Punishment.md | modified | +type: paper; +citekey: Crime and Punishment; +study_type: exome | diseases empty |
| @Cruchaga2012-je.md | modified | +type: paper; +citekey: Cruchaga2012-je; +diseases: 1 | study_type not inferred |
| @Cruchaga2017-sl.md | modified | +type: paper; +citekey: Cruchaga2017-sl; +diseases: 1; +study_type: exome; +n_total: 358; +obs_source: human | — |
| @Cuitavi2021-kd.md | modified | +type: paper; +citekey: Cuitavi2021-kd; +genes: 1; +study_type: review | diseases empty |
| @Cullen2020-rr.md | modified | +type: paper; +citekey: Cullen2020-rr; +diseases: 1; +genes: 1; +study_type: clinical-trial | — |
| @Cullen2021-qa.md | modified | +type: paper; +citekey: Cullen2021-qa; +diseases: 1; +study_type: clinical-trial; +obs_source: human | — |
| @Cummings2019-vv.md | modified | +type: paper; +citekey: Cummings2019-vv; +diseases: 1; +study_type: clinical-trial | — |
| @Dai2019-qa.md | modified | +type: paper; +citekey: Dai2019-qa | diseases empty; study_type not inferred |
| @Dakin2019-mu.md | modified | +type: paper; +citekey: Dakin2019-mu; +study_type: exome | diseases empty |
| @Dalakas2020-jl.md | modified | +type: paper; +citekey: Dalakas2020-jl | diseases empty; study_type not inferred |
| @Dam2021-pp.md | modified | +type: paper; +citekey: Dam2021-pp; +diseases: 1; +study_type: clinical-trial | — |
| @Danis2015-ag.md | modified | +type: paper; +citekey: Danis2015-ag | diseases empty; study_type not inferred |
| @Davey2000-qe.md | modified | +type: paper; +citekey: Davey2000-qe; +obs_source: human | diseases empty; study_type not inferred |
| @Davidoff2016-uy.md | modified | +type: paper; +citekey: Davidoff2016-uy; +genes: 1 | diseases empty; study_type not inferred |
| @Davies2019-gu.md | modified | +type: paper; +citekey: Davies2019-gu | diseases empty; study_type not inferred |
| @Davis2020-rn.md | modified | +type: paper; +citekey: Davis2020-rn; +diseases: 1; +genes: 2; +study_type: functional; +obs_source: human | — |
| @De_Jager2009-au.md | modified | +type: paper; +citekey: De_Jager2009-au | diseases empty; study_type not inferred |
| @De_Jager2009-lt.md | modified | +type: paper; +citekey: De_Jager2009-lt; +diseases: 1; +genes: 1; +obs_source: human | study_type not inferred |
| @De_Jong2021-hh.md | modified | +type: paper; +citekey: De_Jong2021-hh; +diseases: 1; +study_type: review | — |
| @De_Paiva_Lopes2020-os.md | modified | +type: paper; +citekey: De_Paiva_Lopes2020-os | diseases empty; study_type not inferred |
| @De_Rojas2021-tw.md | modified | +type: paper; +citekey: De_Rojas2021-tw; +diseases: 1; +genes: 1; +n_total: 58188; +obs_source: human | study_type not inferred |
| @De_Schepper2020-ka.md | modified | +type: paper; +citekey: De_Schepper2020-ka; +diseases: 1; +genes: 5 | study_type not inferred |
| @De_la_Fuente2021-zs.md | modified | +type: paper; +citekey: De_la_Fuente2021-zs | diseases empty; study_type not inferred |
| @Debette2022-kd.md | modified | +type: paper; +citekey: Debette2022-kd; +study_type: gwas | diseases empty |
| @Decourt2021-kp.md | modified | +type: paper; +citekey: Decourt2021-kp | diseases empty; study_type not inferred |
| @Deczkowska2018-of.md | modified | +type: paper; +citekey: Deczkowska2018-of; +diseases: 1; +genes: 1; +study_type: functional; +obs_source: human | — |
| @Deczkowska2020-pp.md | modified | +type: paper; +citekey: Deczkowska2020-pp | diseases empty; study_type not inferred |
| @Deep Work.md | modified | +type: paper; +citekey: Deep Work | diseases empty; study_type not inferred |
| @Del-Aguila2018-fr.md | modified | +type: paper; +citekey: Del-Aguila2018-fr; +diseases: 1; +study_type: gwas; +obs_source: human | — |
| @Deng2018-yb.md | modified | +type: paper; +citekey: Deng2018-yb | diseases empty; study_type not inferred |
| @Deuschl2020-cg.md | modified | +type: paper; +citekey: Deuschl2020-cg | diseases empty; study_type not inferred |
| @Di-Fonzo2009-nb.md | modified | +type: paper; +citekey: Di-Fonzo2009-nb; +diseases: 1; +genes: 1; +obs_source: human | study_type not inferred |
| @Di_Maio2018-gl.md | modified | +type: paper; +citekey: Di_Maio2018-gl; +diseases: 1 | study_type not inferred |
| @Donaldson2025-wb.md | modified | +type: paper; +citekey: Donaldson2025-wb; +diseases: 1; +obs_source: human | study_type not inferred |
| @Dos_Santos2020-es.md | modified | +type: paper; +citekey: Dos_Santos2020-es | diseases empty; study_type not inferred |
| @Douaud2021-ky.md | modified | +type: paper; +citekey: Douaud2021-ky | diseases empty; study_type not inferred |
| @Dubois2014-mx.md | modified | +type: paper; +citekey: Dubois2014-mx; +diseases: 1 | study_type not inferred |
| @Dufouil2017-xg.md | modified | +type: paper; +citekey: Dufouil2017-xg; +diseases: 2 | study_type not inferred |
| @Dunmore2021-xn.md | modified | +type: paper; +citekey: Dunmore2021-xn; +genes: 1 | diseases empty; study_type not inferred |
| @Ebbert2014-sk.md | modified | +type: paper; +citekey: Ebbert2014-sk | diseases empty; study_type not inferred |
| @Edenberg2013-eq.md | modified | +type: paper; +citekey: Edenberg2013-eq | diseases empty; study_type not inferred |
| @Eggers2023-jh.md | modified | +type: paper; +citekey: Eggers2023-jh; +obs_source: human | diseases empty; study_type not inferred |
| @Eitan2022-jb.md | modified | +type: paper; +citekey: Eitan2022-jb; +diseases: 1; +genes: 3; +study_type: gwas; +n_total: 5774 | — |
| @Ellis2020-rs.md | modified | +type: paper; +citekey: Ellis2020-rs | diseases empty; study_type not inferred |
| @Epi25_Collaborative_Electronic_address_sberkovicunimelbeduau2019-ti.md | modified | +type: paper; +citekey: Epi25_Collaborative_Electronic_address_sberkovicunimelbeduau2019-ti; +study_type: exome; +n_total: 17606 | diseases empty |
| @Escott-Price2015-gn.md | modified | +type: paper; +citekey: Escott-Price2015-gn; +diseases: 1; +study_type: gwas; +n_total: 4603; +obs_source: human | — |
| @Escott-Price2017-op.md | modified | +type: paper; +citekey: Escott-Price2017-op | diseases empty; study_type not inferred |
| @Escott-Price2019-zq.md | modified | +type: paper; +citekey: Escott-Price2019-zq | diseases empty; study_type not inferred |
| @Evans2011-ds.md | modified | +type: paper; +citekey: Evans2011-ds | diseases empty; study_type not inferred |
| @Evans2023-oh.md | modified | +type: paper; +citekey: Evans2023-oh; +diseases: 1; +study_type: clinical-trial; +obs_source: human | — |
| @Eyting2023-ax.md | modified | +type: paper; +citekey: Eyting2023-ax | diseases empty; study_type not inferred |
| @Faissner2019-am.md | modified | +type: paper; +citekey: Faissner2019-am; +diseases: 1 | study_type not inferred |
| @Farfel2016-sj.md | modified | +type: paper; +citekey: Farfel2016-sj | diseases empty; study_type not inferred |
| @Farhan2019-vu.md | modified | +type: paper; +citekey: Farhan2019-vu; +diseases: 1; +genes: 2; +study_type: exome | — |
| @Farrer1997-gm.md | modified | +type: paper; +citekey: Farrer1997-gm; +diseases: 1; +study_type: meta-analysis | — |
| @Fautsch2021-nc.md | modified | +type: paper; +citekey: Fautsch2021-nc; +diseases: 1 | study_type not inferred |
| @Ferguson2020-eo.md | modified | +type: paper; +citekey: Ferguson2020-eo; +diseases: 1; +n_total: 395769 | study_type not inferred |
| @Filippi2018-xy.md | modified | +type: paper; +citekey: Filippi2018-xy; +diseases: 2 | study_type not inferred |
| @Fleckenstein2021-ss.md | modified | +type: paper; +citekey: Fleckenstein2021-ss | diseases empty; study_type not inferred |
| @Flow.md | modified | +type: paper; +citekey: Flow | diseases empty; study_type not inferred |
| @Fortea2024-ng.md | modified | +type: paper; +citekey: Fortea2024-ng; +diseases: 1; +study_type: review | — |
| @Fowler2011-st.md | modified | +type: paper; +citekey: Fowler2011-st | diseases empty; study_type not inferred |
| @Fredrickson2010-oq.md | modified | +type: paper; +citekey: Fredrickson2010-oq | diseases empty; study_type not inferred |
| @Frey2019-zw.md | modified | +type: paper; +citekey: Frey2019-zw | diseases empty; study_type not inferred |
| @Friedman2004-og.md | modified | +type: paper; +citekey: Friedman2004-og | diseases empty; study_type not inferred |
| @Friedman2018-gf.md | modified | +type: paper; +citekey: Friedman2018-gf | diseases empty; study_type not inferred |
| @Friedman2021-ak.md | modified | +type: paper; +citekey: Friedman2021-ak; +genes: 1 | diseases empty; study_type not inferred |
| @Frisoni2022-dt.md | modified | +type: paper; +citekey: Frisoni2022-dt; +diseases: 1 | study_type not inferred |
| @Fritsche2016-vf.md | modified | +type: paper; +citekey: Fritsche2016-vf; +diseases: 1; +study_type: gwas; +obs_source: human | — |
| @Fu2022-ui.md | modified | +type: paper; +citekey: Fu2022-ui; +diseases: 2; +genes: 7; +study_type: exome; +n_total: 91605; +obs_source: human | — |
| @Fujihara2020-dx.md | modified | +type: paper; +citekey: Fujihara2020-dx | diseases empty; study_type not inferred |
| @Fuller1986-sa.md | modified | +type: paper; +citekey: Fuller1986-sa; +diseases: 1; +study_type: clinical-trial; +obs_source: human | — |
| @Furcila2019-lg.md | modified | +type: paper; +citekey: Furcila2019-lg; +diseases: 1; +obs_source: human | study_type not inferred |
| @GBD_2017_US_Neurological_Disorders_Collaborators2020-ns.md | modified | +type: paper; +citekey: GBD_2017_US_Neurological_Disorders_Collaborators2020-ns; +diseases: 7 | study_type not inferred |
| @GBD_2019_Mental_Disorders_Collaborators2022-mi.md | modified | +type: paper; +citekey: GBD_2019_Mental_Disorders_Collaborators2022-mi | diseases empty; study_type not inferred |
| @Gaetani2019-oi.md | modified | +type: paper; +citekey: Gaetani2019-oi; +diseases: 5 | study_type not inferred |
| @Galatro2017-bd.md | modified | +type: paper; +citekey: Galatro2017-bd; +study_type: exome; +obs_source: human | diseases empty |
| @Garbers2018-no.md | modified | +type: paper; +citekey: Garbers2018-no | diseases empty; study_type not inferred |
| @Garcia2017-wv.md | modified | +type: paper; +citekey: Garcia2017-wv; +diseases: 1; +study_type: clinical-trial | — |
| @Geerlings2017-zh.md | modified | +type: paper; +citekey: Geerlings2017-zh; +diseases: 1; +study_type: review | — |
| @Genetic-Modifiers-of-Huntington-s-Disease-GeM-HD-Consortium2015-so.md | modified | +type: paper; +citekey: Genetic-Modifiers-of-Huntington-s-Disease-GeM-HD-Consortium2015-so; +diseases: 1; +genes: 1; +study_type: gwas; +obs_source: human | — |
| @Genetic-Modifiers-of-Huntington-s-Disease-GeM-HD-Consortium2025-ui.md | modified | +type: paper; +citekey: Genetic-Modifiers-of-Huntington-s-Disease-GeM-HD-Consortium2025-ui; +diseases: 1 | study_type not inferred |
| @Genetic_Modifiers_of_Huntingtons_Disease_GeM-HD_Consortium_Electronic_address_gusellahelixmghharvardedu2019-gr.md | modified | +type: paper; +citekey: Genetic_Modifiers_of_Huntingtons_Disease_GeM-HD_Consortium_Electronic_address_gusellahelixmghharvardedu2019-gr; +diseases: 1; +genes: 4 | study_type not inferred |
| @Genin2011-cc.md | modified | +type: paper; +citekey: Genin2011-cc; +diseases: 1; +genes: 1; +study_type: clinical-trial | — |
| @Genovese2010-nz.md | modified | +type: paper; +citekey: Genovese2010-nz; +genes: 1 | diseases empty; study_type not inferred |
| @George C. Marshall, Defender of the Republic.md | modified | +type: paper; +citekey: George C. Marshall, Defender of the Republic | diseases empty; study_type not inferred |
| @George2020-un.md | modified | +type: paper; +citekey: George2020-un | diseases empty; study_type not inferred |
| @George2020-unin.md | modified | +type: paper; +citekey: George2020-unin | diseases empty; study_type not inferred |
| @Germain2014-gb.md | modified | +type: paper; +citekey: Germain2014-gb; +diseases: 1 | study_type not inferred |
| @Getz2016-re.md | modified | +type: paper; +citekey: Getz2016-re; +diseases: 1; +study_type: functional | — |
| @Gharahkhani2021-ep.md | modified | +type: paper; +citekey: Gharahkhani2021-ep; +diseases: 1; +study_type: gwas | — |
| @Ghosh2020-mt.md | modified | +type: paper; +citekey: Ghosh2020-mt | diseases empty; study_type not inferred |
| @Gianfrancesco2017-nn.md | modified | +type: paper; +citekey: Gianfrancesco2017-nn | diseases empty; study_type not inferred |
| @Gijselinck2018-yc.md | modified | +type: paper; +citekey: Gijselinck2018-yc | diseases empty; study_type not inferred |
| @Gillmore2021-qv.md | modified | +type: paper; +citekey: Gillmore2021-qv; +diseases: 1; +study_type: clinical-trial; +n_total: 26146; +obs_source: human | — |
| @Giraldo2013-if.md | modified | +type: paper; +citekey: Giraldo2013-if; +diseases: 1; +obs_source: human | study_type not inferred |
| @Glockner2002-jv.md | modified | +type: paper; +citekey: Glockner2002-jv | diseases empty; study_type not inferred |
| @Goadsby2009-ee.md | modified | +type: paper; +citekey: Goadsby2009-ee; +diseases: 1; +study_type: clinical-trial; +n_total: 65; +obs_source: human | — |
| @Goedde1979-rq.md | modified | +type: paper; +citekey: Goedde1979-rq | diseases empty; study_type not inferred |
| @Goedert2018-ks.md | modified | +type: paper; +citekey: Goedert2018-ks; +diseases: 1; +study_type: review | — |
| @Gold2018-dx.md | modified | +type: paper; +citekey: Gold2018-dx; +diseases: 3; +study_type: clinical-trial | — |
| @Gooch2017-ng.md | modified | +type: paper; +citekey: Gooch2017-ng | diseases empty; study_type not inferred |
| @Gorman2022-vi.md | modified | +type: paper; +citekey: Gorman2022-vi; +diseases: 1; +genes: 2; +study_type: gwas; +n_total: 425720; +obs_source: human | — |
| @Grapes of Wrath.md | modified | +type: paper; +citekey: Grapes of Wrath | diseases empty; study_type not inferred |
| @Grassmann2015-fh.md | modified | +type: paper; +citekey: Grassmann2015-fh | diseases empty; study_type not inferred |
| @Greenhalgh2020-cv.md | modified | +type: paper; +citekey: Greenhalgh2020-cv | diseases empty; study_type not inferred |
| @Grill2019-jp.md | modified | +type: paper; +citekey: Grill2019-jp | diseases empty; study_type not inferred |
| @Grove2019-aq.md | modified | +type: paper; +citekey: Grove2019-aq; +diseases: 2 | study_type not inferred |
| @Guerreiro2013-ix.md | modified | +type: paper; +citekey: Guerreiro2013-ix; +diseases: 1; +genes: 1 | study_type not inferred |
| @Guerreiro2013-zf.md | modified | +type: paper; +citekey: Guerreiro2013-zf; +diseases: 1; +genes: 1; +study_type: exome; +obs_source: human | — |
| @Hagen2019-mg.md | modified | +type: paper; +citekey: Hagen2019-mg | diseases empty; study_type not inferred |
| @Hammond2019-ig.md | modified | +type: paper; +citekey: Hammond2019-ig | diseases empty; study_type not inferred |
| @Han2019-fy.md | modified | +type: paper; +citekey: Han2019-fy; +diseases: 1; +genes: 1; +n_total: 786 | study_type not inferred |
| @Han2023-ks.md | modified | +type: paper; +citekey: Han2023-ks | diseases empty; study_type not inferred |
| @Hansen2018-na.md | modified | +type: paper; +citekey: Hansen2018-na | diseases empty; study_type not inferred |
| @Hanson2018-tq.md | modified | +type: paper; +citekey: Hanson2018-tq | diseases empty; study_type not inferred |
| @Hansson2021-nk.md | modified | +type: paper; +citekey: Hansson2021-nk; +genes: 1; +study_type: review; +obs_source: human | diseases empty |
| @Hansson2023-br.md | modified | +type: paper; +citekey: Hansson2023-br; +diseases: 1 | study_type not inferred |
| @Hao2015-sn.md | modified | +type: paper; +citekey: Hao2015-sn | diseases empty; study_type not inferred |
| @Harb2019-wd.md | modified | +type: paper; +citekey: Harb2019-wd | diseases empty; study_type not inferred |
| @Hardy2019-tm.md | modified | +type: paper; +citekey: Hardy2019-tm; +diseases: 1 | study_type not inferred |
| @Hardy2022-oo.md | modified | +type: paper; +citekey: Hardy2022-oo; +diseases: 1 | study_type not inferred |
| @Hardy2023-me.md | modified | +type: paper; +citekey: Hardy2023-me; +diseases: 1 | study_type not inferred |
| @Harold2009-sa.md | modified | +type: paper; +citekey: Harold2009-sa; +diseases: 1; +study_type: gwas; +n_total: 11789 | — |
| @Harper2015-nk.md | modified | +type: paper; +citekey: Harper2015-nk | diseases empty; study_type not inferred |
| @Harrison2020-ji.md | modified | +type: paper; +citekey: Harrison2020-ji; +diseases: 1; +study_type: review; +obs_source: human | — |
| @Hasselmann2019-mz.md | modified | +type: paper; +citekey: Hasselmann2019-mz; +genes: 1; +study_type: functional; +obs_source: human | diseases empty |
| @Hauge2009-mq.md | modified | +type: paper; +citekey: Hauge2009-mq; +diseases: 1; +study_type: clinical-trial; +obs_source: human | — |
| @Hauser2017-ri.md | modified | +type: paper; +citekey: Hauser2017-ri | diseases empty; study_type not inferred |
| @Hauser2020-yo.md | modified | +type: paper; +citekey: Hauser2020-yo; +diseases: 2; +study_type: review | — |
| @Hautakangas2022-dg.md | modified | +type: paper; +citekey: Hautakangas2022-dg; +diseases: 1; +study_type: gwas | — |
| @Heagerty_undated-lf.md | modified | +type: paper; +citekey: Heagerty_undated-lf | diseases empty; study_type not inferred |
| @Hebert2013-as.md | modified | +type: paper; +citekey: Hebert2013-as; +diseases: 1 | study_type not inferred |
| @Hedstrom2019-bo.md | modified | +type: paper; +citekey: Hedstrom2019-bo | diseases empty; study_type not inferred |
| @Heesterbeek2020-jc.md | modified | +type: paper; +citekey: Heesterbeek2020-jc; +diseases: 1; +study_type: review; +obs_source: human | — |
| @Herbort2017-jw.md | modified | +type: paper; +citekey: Herbort2017-jw | diseases empty; study_type not inferred |
| @Herrup2015-om.md | modified | +type: paper; +citekey: Herrup2015-om | diseases empty; study_type not inferred |
| @Hoeper2023-kb.md | modified | +type: paper; +citekey: Hoeper2023-kb; +diseases: 1; +study_type: clinical-trial | — |
| @Hoffmann2016-av.md | modified | +type: paper; +citekey: Hoffmann2016-av; +study_type: gwas | diseases empty |
| @Hoglinger2021-ca.md | modified | +type: paper; +citekey: Hoglinger2021-ca; +diseases: 1; +study_type: clinical-trial | — |
| @Hollingworth2011-wr.md | modified | +type: paper; +citekey: Hollingworth2011-wr; +diseases: 1; +genes: 5 | study_type not inferred |
| @Holstege2020-ky.md | modified | +type: paper; +citekey: Holstege2020-ky; +diseases: 1; +genes: 5; +study_type: gwas; +n_total: 32558 | — |
| @Holtzman2012-dx.md | modified | +type: paper; +citekey: Holtzman2012-dx | diseases empty; study_type not inferred |
| @Hong2016-wf.md | modified | +type: paper; +citekey: Hong2016-wf | diseases empty; study_type not inferred |
| @Hou2019-mo.md | modified | +type: paper; +citekey: Hou2019-mo; +diseases: 1; +study_type: gwas | — |
| @Howard2018-yz.md | modified | +type: paper; +citekey: Howard2018-yz; +diseases: 1; +genes: 4; +study_type: gwas; +obs_source: human | — |
| @Huckins2018-ha.md | modified | +type: paper; +citekey: Huckins2018-ha | diseases empty; study_type not inferred |
| @Huentelman2020-cw.md | modified | +type: paper; +citekey: Huentelman2020-cw | diseases empty; study_type not inferred |
| @Hui2023-lq.md | modified | +type: paper; +citekey: Hui2023-lq | diseases empty; study_type not inferred |
| @Hujoel2024-iv.md | modified | +type: paper; +citekey: Hujoel2024-iv | diseases empty; study_type not inferred |
| @Humbert2021-ou.md | modified | +type: paper; +citekey: Humbert2021-ou | diseases empty; study_type not inferred |
| @Hung2023-bd.md | modified | +type: paper; +citekey: Hung2023-bd; +diseases: 1 | study_type not inferred |
| @Huynh2017-ld.md | modified | +type: paper; +citekey: Huynh2017-ld | diseases empty; study_type not inferred |
| @Hysi2020-ye.md | modified | +type: paper; +citekey: Hysi2020-ye; +diseases: 4; +genes: 4; +study_type: gwas; +n_total: 30; +obs_source: human | — |
| @Imamura2021-kl.md | modified | +type: paper; +citekey: Imamura2021-kl; +study_type: gwas; +n_total: 2983 | diseases empty |
| @In Cold Blood.md | modified | +type: paper; +citekey: In Cold Blood | diseases empty; study_type not inferred |
| @Infinite Jest.md | modified | +type: paper; +citekey: Infinite Jest | diseases empty; study_type not inferred |
| @Infinite Powers.md | modified | +type: paper; +citekey: Infinite Powers | diseases empty; study_type not inferred |
| @Insel2020-vr.md | modified | +type: paper; +citekey: Insel2020-vr; +diseases: 1; +obs_source: human | study_type not inferred |
| @International_League_Against_Epilepsy_Consortium_on_Complex_Epilepsies2018-us.md | modified | +type: paper; +citekey: International_League_Against_Epilepsy_Consortium_on_Complex_Epilepsies2018-us | diseases empty; study_type not inferred |
| @International_Multiple_Sclerosis_Genetics_Consortium2007-gg.md | modified | +type: paper; +citekey: International_Multiple_Sclerosis_Genetics_Consortium2007-gg; +diseases: 1; +genes: 1; +study_type: gwas | — |
| @International_Multiple_Sclerosis_Genetics_Consortium2011-ar.md | modified | +type: paper; +citekey: International_Multiple_Sclerosis_Genetics_Consortium2011-ar; +study_type: gwas; +n_total: 27148 | diseases empty |
| @International_Multiple_Sclerosis_Genetics_Consortium2019-cg.md | modified | +type: paper; +citekey: International_Multiple_Sclerosis_Genetics_Consortium2019-cg; +diseases: 1; +study_type: gwas; +n_total: 41505; +obs_source: human | — |
| @International_Multiple_Sclerosis_Genetics_Consortium_Electronic_address_chriscotsapasyaleedu2018-pu.md | modified | +type: paper; +citekey: International_Multiple_Sclerosis_Genetics_Consortium_Electronic_address_chriscotsapasyaleedu2018-pu; +diseases: 1; +genes: 6; +study_type: gwas | — |
| @International_Multiple_Sclerosis_Genetics_Consortium_IMSGC2013-ff.md | modified | +type: paper; +citekey: International_Multiple_Sclerosis_Genetics_Consortium_IMSGC2013-ff; +diseases: 1; +n_total: 80094 | study_type not inferred |
| @International_Parkinson_Disease_Genomics_Consortium2011-ih.md | modified | +type: paper; +citekey: International_Parkinson_Disease_Genomics_Consortium2011-ih; +diseases: 1; +study_type: gwas | — |
| @Iram2022-xf.md | modified | +type: paper; +citekey: Iram2022-xf; +diseases: 3; +study_type: clinical-trial | — |
| @Ivarsdottir2021-dk.md | modified | +type: paper; +citekey: Ivarsdottir2021-dk; +study_type: gwas | diseases empty |
| @Jack2018-au.md | modified | +type: paper; +citekey: Jack2018-au; +diseases: 1 | study_type not inferred |
| @Jack2019-nm.md | modified | +type: paper; +citekey: Jack2019-nm | diseases empty; study_type not inferred |
| @Jadhav2019-gs.md | modified | +type: paper; +citekey: Jadhav2019-gs | diseases empty; study_type not inferred |
| @Janelidze2020-er.md | modified | +type: paper; +citekey: Janelidze2020-er; +diseases: 1; +obs_source: human | study_type not inferred |
| @Janelidze2020-zr.md | modified | +type: paper; +citekey: Janelidze2020-zr; +diseases: 1; +n_total: 194 | study_type not inferred |
| @Janelidze2021-qn.md | modified | +type: paper; +citekey: Janelidze2021-qn; +diseases: 1; +study_type: clinical-trial; +obs_source: human | — |
| @Jansen2015-oy.md | modified | +type: paper; +citekey: Jansen2015-oy; +diseases: 1; +study_type: meta-analysis | — |
| @Jansen2019-pf.md | modified | +type: paper; +citekey: Jansen2019-pf; +diseases: 1; +study_type: meta-analysis; +n_total: 79145; +obs_source: human | — |
| @Jaschke2021-cx.md | modified | +type: paper; +citekey: Jaschke2021-cx | diseases empty; study_type not inferred |
| @Jelcic2018-ye.md | modified | +type: paper; +citekey: Jelcic2018-ye; +diseases: 2 | study_type not inferred |
| @Jessen2010-fj.md | modified | +type: paper; +citekey: Jessen2010-fj | diseases empty; study_type not inferred |
| @Jessen2014-nm.md | modified | +type: paper; +citekey: Jessen2014-nm | diseases empty; study_type not inferred |
| @Jessen2020-il.md | modified | +type: paper; +citekey: Jessen2020-il; +diseases: 1; +study_type: meta-analysis | — |
| @Jiang2020-xd.md | modified | +type: paper; +citekey: Jiang2020-xd; +genes: 1; +obs_source: human | diseases empty; study_type not inferred |
| @Jimenez-Maggiora2020-pi.md | modified | +type: paper; +citekey: Jimenez-Maggiora2020-pi; +obs_source: human | diseases empty; study_type not inferred |
| @Johnson2023-ri.md | modified | +type: paper; +citekey: Johnson2023-ri; +diseases: 1 | study_type not inferred |
| @Johnston2019-lj.md | modified | +type: paper; +citekey: Johnston2019-lj; +study_type: gwas; +obs_source: human | diseases empty |
| @Johnston2021-fl.md | modified | +type: paper; +citekey: Johnston2021-fl | diseases empty; study_type not inferred |
| @Jonsson2012-dj.md | modified | +type: paper; +citekey: Jonsson2012-dj; +diseases: 1 | study_type not inferred |
| @Jonsson2013-je.md | modified | +type: paper; +citekey: Jonsson2013-je; +diseases: 1; +genes: 1 | study_type not inferred |
| @Jordan2018-gk.md | modified | +type: paper; +citekey: Jordan2018-gk | diseases empty; study_type not inferred |
| @Jorgensen2011-qm.md | modified | +type: paper; +citekey: Jorgensen2011-qm | diseases empty; study_type not inferred |
| @Jorgenson2017-yn.md | modified | +type: paper; +citekey: Jorgenson2017-yn; +genes: 2; +study_type: gwas; +n_total: 71; +obs_source: human | diseases empty |
| @Joseph2018-jk.md | modified | +type: paper; +citekey: Joseph2018-jk; +diseases: 1; +genes: 1 | study_type not inferred |
| @Jurcau2022-hf.md | modified | +type: paper; +citekey: Jurcau2022-hf; +diseases: 1; +study_type: review; +obs_source: human | — |
| @Jurga2020-xo.md | modified | +type: paper; +citekey: Jurga2020-xo; +study_type: review; +obs_source: human | diseases empty |
| @Kaneko2010-tn.md | modified | +type: paper; +citekey: Kaneko2010-tn | diseases empty; study_type not inferred |
| @Karch2018-fk.md | modified | +type: paper; +citekey: Karch2018-fk | diseases empty; study_type not inferred |
| @Karczewski2020-ko.md | modified | +type: paper; +citekey: Karczewski2020-ko | diseases empty; study_type not inferred |
| @Karikari2020-zq.md | modified | +type: paper; +citekey: Karikari2020-zq; +diseases: 4; +study_type: exome; +n_total: 1131 | — |
| @Karran2022-xa.md | modified | +type: paper; +citekey: Karran2022-xa; +diseases: 1; +study_type: clinical-trial | — |
| @Katoh2006-tt.md | modified | +type: paper; +citekey: Katoh2006-tt | diseases empty; study_type not inferred |
| @Katzourou2021-va.md | modified | +type: paper; +citekey: Katzourou2021-va; +diseases: 1; +genes: 1; +n_total: 616; +obs_source: human | study_type not inferred |
| @Kay2015-zz.md | modified | +type: paper; +citekey: Kay2015-zz; +diseases: 1 | study_type not inferred |
| @Kay2019-iw.md | modified | +type: paper; +citekey: Kay2019-iw; +diseases: 1; +obs_source: human | study_type not inferred |
| @Keane2016-yt.md | modified | +type: paper; +citekey: Keane2016-yt; +study_type: review | diseases empty |
| @Keenan2018-ak.md | modified | +type: paper; +citekey: Keenan2018-ak; +diseases: 1; +study_type: clinical-trial | — |
| @Keller2022-ze.md | modified | +type: paper; +citekey: Keller2022-ze | diseases empty; study_type not inferred |
| @Kelley2019-rr.md | modified | +type: paper; +citekey: Kelley2019-rr | diseases empty; study_type not inferred |
| @Kelsell1997-di.md | modified | +type: paper; +citekey: Kelsell1997-di | diseases empty; study_type not inferred |
| @Kepp2022-dh.md | modified | +type: paper; +citekey: Kepp2022-dh | diseases empty; study_type not inferred |
| @Kepp2023-fp.md | modified | +type: paper; +citekey: Kepp2023-fp; +study_type: review | diseases empty |
| @Keren-Shaul2017-zq.md | modified | +type: paper; +citekey: Keren-Shaul2017-zq; +diseases: 1 | study_type not inferred |
| @Khaled2021-hk.md | modified | +type: paper; +citekey: Khaled2021-hk; +diseases: 1 | study_type not inferred |
| @Khalil2018-tn.md | modified | +type: paper; +citekey: Khalil2018-tn; +diseases: 1; +genes: 1 | study_type not inferred |
| @Khalil2021-mv.md | modified | +type: paper; +citekey: Khalil2021-mv; +diseases: 1; +obs_source: human | study_type not inferred |
| @Khalil2024-nd.md | modified | +type: paper; +citekey: Khalil2024-nd | diseases empty; study_type not inferred |
| @Khan2013-iw.md | modified | +type: paper; +citekey: Khan2013-iw; +study_type: review; +n_total: 60883; +obs_source: human | diseases empty |
| @Kim2007-nx.md | modified | +type: paper; +citekey: Kim2007-nx | diseases empty; study_type not inferred |
| @Kim2018-cc.md | modified | +type: paper; +citekey: Kim2018-cc; +genes: 1; +study_type: functional | diseases empty |
| @Kitsos2010-uj.md | modified | +type: paper; +citekey: Kitsos2010-uj; +diseases: 1; +study_type: exome | — |
| @Kleinberger2014-hh.md | modified | +type: paper; +citekey: Kleinberger2014-hh | diseases empty; study_type not inferred |
| @Kluss2019-hk.md | modified | +type: paper; +citekey: Kluss2019-hk; +diseases: 1; +genes: 1 | study_type not inferred |
| @Knopman2020-mk.md | modified | +type: paper; +citekey: Knopman2020-mk | diseases empty; study_type not inferred |
| @Knopman2021-fu.md | modified | +type: paper; +citekey: Knopman2021-fu; +diseases: 1 | study_type not inferred |
| @Ko2017-rp.md | modified | +type: paper; +citekey: Ko2017-rp; +diseases: 1 | study_type not inferred |
| @Ko2018-an.md | modified | +type: paper; +citekey: Ko2018-an | diseases empty; study_type not inferred |
| @Kostich2016-ml.md | modified | +type: paper; +citekey: Kostich2016-ml; +genes: 1; +study_type: exome | diseases empty |
| @Kranzler2018-gl.md | modified | +type: paper; +citekey: Kranzler2018-gl | diseases empty; study_type not inferred |
| @Kranzler2019-gt.md | modified | +type: paper; +citekey: Kranzler2019-gt; +diseases: 1; +study_type: gwas; +n_total: 274424 | — |
| @Krysinska2017-eh.md | modified | +type: paper; +citekey: Krysinska2017-eh; +study_type: review; +n_total: 2967 | diseases empty |
| @Kuiper2018-xj.md | modified | +type: paper; +citekey: Kuiper2018-xj | diseases empty; study_type not inferred |
| @Kuiper2020-hk.md | modified | +type: paper; +citekey: Kuiper2020-hk; +study_type: exome | diseases empty |
| @Kunkle2019-at.md | modified | +type: paper; +citekey: Kunkle2019-at; +diseases: 1; +study_type: gwas; +n_total: 94437 | — |
| @Kuo2020-jx.md | modified | +type: paper; +citekey: Kuo2020-jx | diseases empty; study_type not inferred |
| @Lambert2009-wv.md | modified | +type: paper; +citekey: Lambert2009-wv; +diseases: 1; +study_type: gwas; +n_total: 7275 | — |
| @Lambert2013-ax.md | modified | +type: paper; +citekey: Lambert2013-ax; +diseases: 1; +study_type: meta-analysis; +n_total: 74046 | — |
| @Lambert2023-yx.md | modified | +type: paper; +citekey: Lambert2023-yx; +diseases: 1 | study_type not inferred |
| @Langbaum2019-ct.md | modified | +type: paper; +citekey: Langbaum2019-ct | diseases empty; study_type not inferred |
| @Langbehn2022-kh.md | modified | +type: paper; +citekey: Langbehn2022-kh | diseases empty; study_type not inferred |
| @Langford2020-rw.md | modified | +type: paper; +citekey: Langford2020-rw; +diseases: 1; +obs_source: human | study_type not inferred |
| @Late Bloomers.md | modified | +type: paper; +citekey: Late Bloomers | diseases empty; study_type not inferred |
| @Le_Guen2022-dm.md | modified | +type: paper; +citekey: Le_Guen2022-dm; +diseases: 1 | study_type not inferred |
| @Lee2012-tu.md | modified | +type: paper; +citekey: Lee2012-tu; +diseases: 1 | study_type not inferred |
| @Lee2017-ww.md | modified | +type: paper; +citekey: Lee2017-ww; +diseases: 1; +study_type: functional | — |
| @Lee2019-xf.md | modified | +type: paper; +citekey: Lee2019-xf | diseases empty; study_type not inferred |
| @Lee2022-fv.md | modified | +type: paper; +citekey: Lee2022-fv | diseases empty; study_type not inferred |
| @Leipold2013-rn.md | modified | +type: paper; +citekey: Leipold2013-rn; +genes: 1; +study_type: exome | diseases empty |
| @Leng2021-ua.md | modified | +type: paper; +citekey: Leng2021-ua; +diseases: 1 | study_type not inferred |
| @Leonenko2021-ob.md | modified | +type: paper; +citekey: Leonenko2021-ob; +diseases: 1; +study_type: exome; +n_total: 549; +obs_source: human | — |
| @Lesman-Segev2021-it.md | modified | +type: paper; +citekey: Lesman-Segev2021-it | diseases empty; study_type not inferred |
| @Lettice2002-ho.md | modified | +type: paper; +citekey: Lettice2002-ho | diseases empty; study_type not inferred |
| @Leuzy2022-kt.md | modified | +type: paper; +citekey: Leuzy2022-kt; +diseases: 1 | study_type not inferred |
| @Levey2021-dm.md | modified | +type: paper; +citekey: Levey2021-dm; +study_type: gwas | diseases empty |
| @Lewcock2020-hp.md | modified | +type: paper; +citekey: Lewcock2020-hp; +diseases: 1; +genes: 3 | study_type not inferred |
| @Lewis2005-rs.md | modified | +type: paper; +citekey: Lewis2005-rs; +genes: 1; +study_type: meta-analysis | diseases empty |
| @Lewis2022-er.md | modified | +type: paper; +citekey: Lewis2022-er | diseases empty; study_type not inferred |
| @Lewis2023-jo.md | modified | +type: paper; +citekey: Lewis2023-jo; +study_type: exome | diseases empty |
| @Li2017-ym.md | modified | +type: paper; +citekey: Li2017-ym | diseases empty; study_type not inferred |
| @Li2019-xs.md | modified | +type: paper; +citekey: Li2019-xs | diseases empty; study_type not inferred |
| @Li2021-di.md | modified | +type: paper; +citekey: Li2021-di; +diseases: 1 | study_type not inferred |
| @Liao2015-rw.md | modified | +type: paper; +citekey: Liao2015-rw; +diseases: 1; +study_type: functional; +obs_source: human | — |
| @Liao2018-wo.md | modified | +type: paper; +citekey: Liao2018-wo | diseases empty; study_type not inferred |
| @Lim2012-eg.md | modified | +type: paper; +citekey: Lim2012-eg; +diseases: 2 | study_type not inferred |
| @Lim2019-ze.md | modified | +type: paper; +citekey: Lim2019-ze; +diseases: 1; +n_total: 1450 | study_type not inferred |
| @Lin2020-rn.md | modified | +type: paper; +citekey: Lin2020-rn | diseases empty; study_type not inferred |
| @Lin2024-lc.md | modified | +type: paper; +citekey: Lin2024-lc | diseases empty; study_type not inferred |
| @Littlejohns2020-he.md | modified | +type: paper; +citekey: Littlejohns2020-he; +obs_source: human | diseases empty; study_type not inferred |
| @Liu2013-av.md | modified | +type: paper; +citekey: Liu2013-av | diseases empty; study_type not inferred |
| @Liu2019-fk.md | modified | +type: paper; +citekey: Liu2019-fk | diseases empty; study_type not inferred |
| @Liu2019-pf.md | modified | +type: paper; +citekey: Liu2019-pf; +genes: 1 | diseases empty; study_type not inferred |
| @Liu2019-rd.md | modified | +type: paper; +citekey: Liu2019-rd | diseases empty; study_type not inferred |
| @Liu2021-qt.md | modified | +type: paper; +citekey: Liu2021-qt | diseases empty; study_type not inferred |
| @Lives of the Popes.md | modified | +type: paper; +citekey: Lives of the Popes | diseases empty; study_type not inferred |
| @Livingston2020-kk.md | modified | +type: paper; +citekey: Livingston2020-kk; +diseases: 1; +obs_source: human | study_type not inferred |
| @Llibre-Guerra2019-tc.md | modified | +type: paper; +citekey: Llibre-Guerra2019-tc; +diseases: 1 | study_type not inferred |
| @Long2022-ie.md | modified | +type: paper; +citekey: Long2022-ie; +diseases: 1 | study_type not inferred |
| @Lopez_de_Castro2018-mu.md | modified | +type: paper; +citekey: Lopez_de_Castro2018-mu | diseases empty; study_type not inferred |
| @Lou2016-fc.md | modified | +type: paper; +citekey: Lou2016-fc; +genes: 1 | diseases empty; study_type not inferred |
| @Lumsden2020-yc.md | modified | +type: paper; +citekey: Lumsden2020-yc; +study_type: meta-analysis; +n_total: 153; +obs_source: human | diseases empty |
| @Luo2022-cq.md | modified | +type: paper; +citekey: Luo2022-cq; +diseases: 1; +n_total: 2609 | study_type not inferred |
| @Lupton2020-ps.md | modified | +type: paper; +citekey: Lupton2020-ps; +diseases: 1; +study_type: gwas; +n_total: 250 | — |
| @Lv2024-ja.md | modified | +type: paper; +citekey: Lv2024-ja | diseases empty; study_type not inferred |
| @MacGregor2018-bq.md | modified | +type: paper; +citekey: MacGregor2018-bq | diseases empty; study_type not inferred |
| @Macauley2014-wj.md | modified | +type: paper; +citekey: Macauley2014-wj | diseases empty; study_type not inferred |
| @Macbeth.md | modified | +type: paper; +citekey: Macbeth | diseases empty; study_type not inferred |
| @Mackin2018-uz.md | modified | +type: paper; +citekey: Mackin2018-uz | diseases empty; study_type not inferred |
| @Magalhaes2022-iy.md | modified | +type: paper; +citekey: Magalhaes2022-iy | diseases empty; study_type not inferred |
| @Magrinelli2024-ok.md | modified | +type: paper; +citekey: Magrinelli2024-ok; +diseases: 1; +genes: 1 | study_type not inferred |
| @Mahley2016-af.md | modified | +type: paper; +citekey: Mahley2016-af; +study_type: review | diseases empty |
| @Malik2021-pa.md | modified | +type: paper; +citekey: Malik2021-pa | diseases empty; study_type not inferred |
| @Mansournia2018-uf.md | modified | +type: paper; +citekey: Mansournia2018-uf | diseases empty; study_type not inferred |
| @Marais2019-cg.md | modified | +type: paper; +citekey: Marais2019-cg; +study_type: review; +obs_source: human | diseases empty |
| @Marioni2018-ml.md | modified | +type: paper; +citekey: Marioni2018-ml; +diseases: 1; +study_type: gwas | — |
| @Marras2018-sk.md | modified | +type: paper; +citekey: Marras2018-sk | diseases empty; study_type not inferred |
| @Marsh2022-gk.md | modified | +type: paper; +citekey: Marsh2022-gk; +genes: 1 | diseases empty; study_type not inferred |
| @Martens2022-hq.md | modified | +type: paper; +citekey: Martens2022-hq; +diseases: 1; +genes: 1; +study_type: review; +obs_source: human | — |
| @Master of the Senate.md | modified | +type: paper; +citekey: Master of the Senate | diseases empty; study_type not inferred |
| @Masuda2019-zq.md | modified | +type: paper; +citekey: Masuda2019-zq; +diseases: 1; +genes: 3; +obs_source: human | study_type not inferred |
| @Masuda2020-nw.md | modified | +type: paper; +citekey: Masuda2020-nw | diseases empty; study_type not inferred |
| @Masuda2020-rc.md | modified | +type: paper; +citekey: Masuda2020-rc | diseases empty; study_type not inferred |
| @Matcovitch-Natan2016-dx.md | modified | +type: paper; +citekey: Matcovitch-Natan2016-dx | diseases empty; study_type not inferred |
| @Matejcic2017-ss.md | modified | +type: paper; +citekey: Matejcic2017-ss; +genes: 2; +study_type: review; +obs_source: human | diseases empty |
| @Mathys2019-ho.md | modified | +type: paper; +citekey: Mathys2019-ho; +obs_source: human | diseases empty; study_type not inferred |
| @McAllister2022-fj.md | modified | +type: paper; +citekey: McAllister2022-fj | diseases empty; study_type not inferred |
| @McCauley2023-ih.md | modified | +type: paper; +citekey: McCauley2023-ih | diseases empty; study_type not inferred |
| @McCoy2018-yq.md | modified | +type: paper; +citekey: McCoy2018-yq | diseases empty; study_type not inferred |
| @McHarg2015-yi.md | modified | +type: paper; +citekey: McHarg2015-yi; +diseases: 1 | study_type not inferred |
| @Medway2014-pr.md | modified | +type: paper; +citekey: Medway2014-pr; +diseases: 1; +obs_source: human | study_type not inferred |
| @Meissner2019-xz.md | modified | +type: paper; +citekey: Meissner2019-xz; +diseases: 1; +genes: 1; +study_type: review | — |
| @Meng2018-ix.md | modified | +type: paper; +citekey: Meng2018-ix; +genes: 1; +study_type: gwas; +n_total: 560; +obs_source: human | diseases empty |
| @Meng2019-iu.md | modified | +type: paper; +citekey: Meng2019-iu | diseases empty; study_type not inferred |
| @Meng2020-uo.md | modified | +type: paper; +citekey: Meng2020-uo; +study_type: gwas; +n_total: 19598 | diseases empty |
| @Metovic2024-yo.md | modified | +type: paper; +citekey: Metovic2024-yo; +genes: 1; +study_type: clinical-trial | diseases empty |
| @Mielke2024-oy.md | modified | +type: paper; +citekey: Mielke2024-oy | diseases empty; study_type not inferred |
| @Mila-Aloma2022-rb.md | modified | +type: paper; +citekey: Mila-Aloma2022-rb; +diseases: 1; +study_type: exome | — |
| @Miller2020-ok.md | modified | +type: paper; +citekey: Miller2020-ok; +diseases: 1; +study_type: clinical-trial; +n_total: 50 | — |
| @Miller2022-jk.md | modified | +type: paper; +citekey: Miller2022-jk; +diseases: 1; +genes: 1; +obs_source: human | study_type not inferred |
| @Minis2020-ea.md | modified | +type: paper; +citekey: Minis2020-ea; +diseases: 1 | study_type not inferred |
| @Minos2016-hr.md | modified | +type: paper; +citekey: Minos2016-hr | diseases empty; study_type not inferred |
| @Mintun2021-jb.md | modified | +type: paper; +citekey: Mintun2021-jb; +diseases: 1; +study_type: exome | — |
| @Mishra2022-zg.md | modified | +type: paper; +citekey: Mishra2022-zg; +diseases: 1; +study_type: gwas; +n_total: 41 | — |
| @Misra2018-cf.md | modified | +type: paper; +citekey: Misra2018-cf | diseases empty; study_type not inferred |
| @Miyake2020-zt.md | modified | +type: paper; +citekey: Miyake2020-zt; +study_type: functional | diseases empty |
| @Mocumbi2024-ao.md | modified | +type: paper; +citekey: Mocumbi2024-ao; +diseases: 1; +genes: 1 | study_type not inferred |
| @Mokry2015-wy.md | modified | +type: paper; +citekey: Mokry2015-wy | diseases empty; study_type not inferred |
| @Molinuevo2018-cq.md | modified | +type: paper; +citekey: Molinuevo2018-cq; +diseases: 1; +study_type: review | — |
| @Momozawa2021-xs.md | modified | +type: paper; +citekey: Momozawa2021-xs | diseases empty; study_type not inferred |
| @Moreno-Grau2019-my.md | modified | +type: paper; +citekey: Moreno-Grau2019-my; +diseases: 1; +study_type: gwas | — |
| @Moscoso2021-jg.md | modified | +type: paper; +citekey: Moscoso2021-jg; +diseases: 1; +n_total: 1067 | study_type not inferred |
| @Mountjoy2020-em.md | modified | +type: paper; +citekey: Mountjoy2020-em; +study_type: gwas | diseases empty |
| @Moutsianas2015-jl.md | modified | +type: paper; +citekey: Moutsianas2015-jl; +diseases: 1; +n_total: 47850; +obs_source: human | study_type not inferred |
| @Mueller2020-ac.md | modified | +type: paper; +citekey: Mueller2020-ac; +diseases: 1 | study_type not inferred |
| @Mukamel2021-qb.md | modified | +type: paper; +citekey: Mukamel2021-qb; +genes: 2 | diseases empty; study_type not inferred |
| @Mullins2021-ik.md | modified | +type: paper; +citekey: Mullins2021-ik; +diseases: 2; +study_type: gwas | — |
| @Musiek2021-wm.md | modified | +type: paper; +citekey: Musiek2021-wm; +diseases: 1; +study_type: review; +obs_source: human | — |
| @Mutschler2016-sm.md | modified | +type: paper; +citekey: Mutschler2016-sm | diseases empty; study_type not inferred |
| @Nagtegaal2019-vh.md | modified | +type: paper; +citekey: Nagtegaal2019-vh | diseases empty; study_type not inferred |
| @Naito2013-cd.md | modified | +type: paper; +citekey: Naito2013-cd | diseases empty; study_type not inferred |
| @Naj2011-of.md | modified | +type: paper; +citekey: Naj2011-of; +diseases: 1 | study_type not inferred |
| @Nakamura2018-pk.md | modified | +type: paper; +citekey: Nakamura2018-pk; +diseases: 1; +obs_source: human | study_type not inferred |
| @Nalivaeva2013-aj.md | modified | +type: paper; +citekey: Nalivaeva2013-aj | diseases empty; study_type not inferred |
| @Nalls2019-te.md | modified | +type: paper; +citekey: Nalls2019-te; +diseases: 1; +study_type: gwas; +obs_source: human | — |
| @Narasimhan2024-by.md | modified | +type: paper; +citekey: Narasimhan2024-by | diseases empty; study_type not inferred |
| @Neitz2000-wl.md | modified | +type: paper; +citekey: Neitz2000-wl | diseases empty; study_type not inferred |
| @Neitz2011-hv.md | modified | +type: paper; +citekey: Neitz2011-hv; +genes: 3 | diseases empty; study_type not inferred |
| @Neitz2019-ze.md | modified | +type: paper; +citekey: Neitz2019-ze; +study_type: review; +obs_source: human | diseases empty |
| @Neitz2021-sn.md | modified | +type: paper; +citekey: Neitz2021-sn; +diseases: 1 | study_type not inferred |
| @Neueder2017-vv.md | modified | +type: paper; +citekey: Neueder2017-vv; +diseases: 1 | study_type not inferred |
| @Ng2017-zd.md | modified | +type: paper; +citekey: Ng2017-zd | diseases empty; study_type not inferred |
| @Nicolas2016-ew.md | modified | +type: paper; +citekey: Nicolas2016-ew | diseases empty; study_type not inferred |
| @Nicolas2018-ly.md | modified | +type: paper; +citekey: Nicolas2018-ly; +diseases: 1; +genes: 4; +n_total: 80610; +obs_source: human | study_type not inferred |
| @Nikom2023-yr.md | modified | +type: paper; +citekey: Nikom2023-yr; +study_type: review | diseases empty |
| @Nishio2022-dk.md | modified | +type: paper; +citekey: Nishio2022-dk; +genes: 1 | diseases empty; study_type not inferred |
| @Nosheny2020-fq.md | modified | +type: paper; +citekey: Nosheny2020-fq; +diseases: 1; +obs_source: human | study_type not inferred |
| @OBrien2011-wr.md | modified | +type: paper; +citekey: OBrien2011-wr | diseases empty; study_type not inferred |
| @OConnor2020-es.md | modified | +type: paper; +citekey: OConnor2020-es; +diseases: 1; +study_type: exome; +obs_source: human | — |
| @Okbay2022-pi.md | modified | +type: paper; +citekey: Okbay2022-pi | diseases empty; study_type not inferred |
| @Olah2020-xn.md | modified | +type: paper; +citekey: Olah2020-xn; +diseases: 1; +genes: 4; +n_total: 833; +obs_source: human | study_type not inferred |
| @Olanow2017-yv.md | modified | +type: paper; +citekey: Olanow2017-yv; +diseases: 1 | study_type not inferred |
| @Olsson2017-sh.md | modified | +type: paper; +citekey: Olsson2017-sh; +diseases: 1 | study_type not inferred |
| @Ong-Tone2021-uu.md | modified | +type: paper; +citekey: Ong-Tone2021-uu; +diseases: 1 | study_type not inferred |
| @Padmanabhan2020-rz.md | modified | +type: paper; +citekey: Padmanabhan2020-rz; +diseases: 1; +genes: 1 | study_type not inferred |
| @Paganoni2020-iw.md | modified | +type: paper; +citekey: Paganoni2020-iw; +diseases: 1 | study_type not inferred |
| @Pale Fire.md | modified | +type: paper; +citekey: Pale Fire | diseases empty; study_type not inferred |
| @Palmer2021-qk.md | modified | +type: paper; +citekey: Palmer2021-qk; +diseases: 2; +genes: 2; +study_type: gwas; +n_total: 46 | — |
| @Palmer2022-xl.md | modified | +type: paper; +citekey: Palmer2022-xl; +diseases: 2; +genes: 1; +study_type: gwas; +n_total: 121570 | — |
| @Palmqvist2019-mk.md | modified | +type: paper; +citekey: Palmqvist2019-mk; +diseases: 1 | study_type not inferred |
| @Palmqvist2019-yp.md | modified | +type: paper; +citekey: Palmqvist2019-yp; +diseases: 1 | study_type not inferred |
| @Palmqvist2020-to.md | modified | +type: paper; +citekey: Palmqvist2020-to; +diseases: 1; +n_total: 81 | study_type not inferred |
| @Palmqvist2021-xb.md | modified | +type: paper; +citekey: Palmqvist2021-xb; +diseases: 1; +n_total: 340; +obs_source: human | study_type not inferred |
| @Palmqvist2024-ry.md | modified | +type: paper; +citekey: Palmqvist2024-ry; +diseases: 1; +study_type: exome | — |
| @Pangrsic2012-ya.md | modified | +type: paper; +citekey: Pangrsic2012-ya | diseases empty; study_type not inferred |
| @Pappalettera2024-ov.md | modified | +type: paper; +citekey: Pappalettera2024-ov | diseases empty; study_type not inferred |
| @Park2019-fi.md | modified | +type: paper; +citekey: Park2019-fi; +diseases: 1; +genes: 1 | study_type not inferred |
| @Pase2019-iw.md | modified | +type: paper; +citekey: Pase2019-iw; +diseases: 1; +n_total: 367 | study_type not inferred |
| @Patani2023-ro.md | modified | +type: paper; +citekey: Patani2023-ro | diseases empty; study_type not inferred |
| @Path Between the Seas.md | modified | +type: paper; +citekey: Path Between the Seas | diseases empty; study_type not inferred |
| @Perin2020-qp.md | modified | +type: paper; +citekey: Perin2020-qp; +diseases: 1 | study_type not inferred |
| @Perlee2013-uk.md | modified | +type: paper; +citekey: Perlee2013-uk | diseases empty; study_type not inferred |
| @Petersen1999-yv.md | modified | +type: paper; +citekey: Petersen1999-yv | diseases empty; study_type not inferred |
| @Petersen2016-fx.md | modified | +type: paper; +citekey: Petersen2016-fx | diseases empty; study_type not inferred |
| @Petersen2018-yg.md | modified | +type: paper; +citekey: Petersen2018-yg | diseases empty; study_type not inferred |
| @Petit2023-bm.md | modified | +type: paper; +citekey: Petit2023-bm; +diseases: 1 | study_type not inferred |
| @Pettigrew2022-ii.md | modified | +type: paper; +citekey: Pettigrew2022-ii; +diseases: 1 | study_type not inferred |
| @Pfister2009-vl.md | modified | +type: paper; +citekey: Pfister2009-vl; +diseases: 1 | study_type not inferred |
| @Picciotto1995-zg.md | modified | +type: paper; +citekey: Picciotto1995-zg | diseases empty; study_type not inferred |
| @Pluvinage2019-in.md | modified | +type: paper; +citekey: Pluvinage2019-in | diseases empty; study_type not inferred |
| @Poewe2017-um.md | modified | +type: paper; +citekey: Poewe2017-um; +diseases: 1; +n_total: 100000 | study_type not inferred |
| @Pohlkamp2021-jd.md | modified | +type: paper; +citekey: Pohlkamp2021-jd | diseases empty; study_type not inferred |
| @Pollack2019-eg.md | modified | +type: paper; +citekey: Pollack2019-eg; +genes: 1; +study_type: gwas; +n_total: 3246; +obs_source: human | diseases empty |
| @Praveen2022-ip.md | modified | +type: paper; +citekey: Praveen2022-ip | diseases empty; study_type not inferred |
| @Preische2019-kp.md | modified | +type: paper; +citekey: Preische2019-kp; +diseases: 1 | study_type not inferred |
| @Prinz2019-fc.md | modified | +type: paper; +citekey: Prinz2019-fc; +genes: 1; +study_type: review; +obs_source: human | diseases empty |
| @Psycho-Cybernetics.md | modified | +type: paper; +citekey: Psycho-Cybernetics | diseases empty; study_type not inferred |
| @Qi2021-md.md | modified | +type: paper; +citekey: Qi2021-md; +study_type: gwas; +obs_source: human | diseases empty |
| @Qian2017-xv.md | modified | +type: paper; +citekey: Qian2017-xv | diseases empty; study_type not inferred |
| @Rachel Maddow.md | modified | +type: paper; +citekey: Rachel Maddow | diseases empty; study_type not inferred |
| @Racine2016-df.md | modified | +type: paper; +citekey: Racine2016-df; +diseases: 1; +n_total: 70 | study_type not inferred |
| @Rademakers2011-di.md | modified | +type: paper; +citekey: Rademakers2011-di; +genes: 1; +study_type: exome | diseases empty |
| @Rai2020-qh.md | modified | +type: paper; +citekey: Rai2020-qh | diseases empty; study_type not inferred |
| @Rajabli2018-ez.md | modified | +type: paper; +citekey: Rajabli2018-ez | diseases empty; study_type not inferred |
| @Rajan2019-qq.md | modified | +type: paper; +citekey: Rajan2019-qq | diseases empty; study_type not inferred |
| @Rajan2020-kl.md | modified | +type: paper; +citekey: Rajan2020-kl; +diseases: 1 | study_type not inferred |
| @Ramanan2019-xy.md | modified | +type: paper; +citekey: Ramanan2019-xy | diseases empty; study_type not inferred |
| @Raulin2022-kh.md | modified | +type: paper; +citekey: Raulin2022-kh; +diseases: 1; +genes: 2 | study_type not inferred |
| @Reich2018-hk.md | modified | +type: paper; +citekey: Reich2018-hk; +diseases: 1; +study_type: clinical-trial | — |
| @Reiman2020-wh.md | modified | +type: paper; +citekey: Reiman2020-wh | diseases empty; study_type not inferred |
| @Rhead2016-ea.md | modified | +type: paper; +citekey: Rhead2016-ea | diseases empty; study_type not inferred |
| @Rhinn2022-py.md | modified | +type: paper; +citekey: Rhinn2022-py; +genes: 1 | diseases empty; study_type not inferred |
| @Richard2021-nv.md | modified | +type: paper; +citekey: Richard2021-nv; +diseases: 1; +study_type: review; +obs_source: human | — |
| @Rideout2020-gn.md | modified | +type: paper; +citekey: Rideout2020-gn; +diseases: 1; +genes: 1 | study_type not inferred |
| @Ridge2013-iu.md | modified | +type: paper; +citekey: Ridge2013-iu; +diseases: 1 | study_type not inferred |
| @Rigotti2022-lj.md | modified | +type: paper; +citekey: Rigotti2022-lj; +study_type: review | diseases empty |
| @Risacher2013-vq.md | modified | +type: paper; +citekey: Risacher2013-vq; +diseases: 1 | study_type not inferred |
| @Ritchie2016-ma.md | modified | +type: paper; +citekey: Ritchie2016-ma | diseases empty; study_type not inferred |
| @Roberts2008-ti.md | modified | +type: paper; +citekey: Roberts2008-ti | diseases empty; study_type not inferred |
| @Roberts2018-aj.md | modified | +type: paper; +citekey: Roberts2018-aj; +diseases: 1 | study_type not inferred |
| @Robot visions.md | modified | +type: paper; +citekey: Robot visions | diseases empty; study_type not inferred |
| @Rodenburg2018-oi.md | modified | +type: paper; +citekey: Rodenburg2018-oi; +study_type: exome | diseases empty |
| @Rodrigues2020-lo.md | modified | +type: paper; +citekey: Rodrigues2020-lo; +diseases: 1 | study_type not inferred |
| @Rogaeva2007-qt.md | modified | +type: paper; +citekey: Rogaeva2007-qt; +genes: 1 | diseases empty; study_type not inferred |
| @Rosati2017-ti.md | modified | +type: paper; +citekey: Rosati2017-ti; +study_type: review | diseases empty |
| @Rosenbaum2021-ou.md | modified | +type: paper; +citekey: Rosenbaum2021-ou; +diseases: 1; +obs_source: human | study_type not inferred |
| @Saddiki2020-qy.md | modified | +type: paper; +citekey: Saddiki2020-qy; +diseases: 1; +genes: 1; +obs_source: human | study_type not inferred |
| @Salas2019-ve.md | modified | +type: paper; +citekey: Salas2019-ve | diseases empty; study_type not inferred |
| @Salloway2021-wy.md | modified | +type: paper; +citekey: Salloway2021-wy; +diseases: 1; +obs_source: human | study_type not inferred |
| @Salvado2023-cp.md | modified | +type: paper; +citekey: Salvado2023-cp | diseases empty; study_type not inferred |
| @Salvado2024-ig.md | modified | +type: paper; +citekey: Salvado2024-ig; +diseases: 1 | study_type not inferred |
| @Sankowski2019-yu.md | modified | +type: paper; +citekey: Sankowski2019-yu; +genes: 2; +obs_source: human | diseases empty; study_type not inferred |
| @Sanna2010-pj.md | modified | +type: paper; +citekey: Sanna2010-pj | diseases empty; study_type not inferred |
| @Satizabal2016-hd.md | modified | +type: paper; +citekey: Satizabal2016-hd | diseases empty; study_type not inferred |
| @Satterstrom2020-xn.md | modified | +type: paper; +citekey: Satterstrom2020-xn; +diseases: 1; +study_type: exome; +n_total: 35584; +obs_source: human | — |
| @Scearce-Levie2020-oz.md | modified | +type: paper; +citekey: Scearce-Levie2020-oz; +diseases: 1 | study_type not inferred |
| @Scheltens2021-tm.md | modified | +type: paper; +citekey: Scheltens2021-tm; +diseases: 1 | study_type not inferred |
| @Schindler2019-dz.md | modified | +type: paper; +citekey: Schindler2019-dz; +diseases: 1 | study_type not inferred |
| @Schizophrenia_Working_Group_of_the_Psychiatric_Genomics_Consortium2014-nc.md | modified | +type: paper; +citekey: Schizophrenia_Working_Group_of_the_Psychiatric_Genomics_Consortium2014-nc; +diseases: 1 | study_type not inferred |
| @Schwartzentruber2020-op.md | modified | +type: paper; +citekey: Schwartzentruber2020-op; +diseases: 1; +study_type: gwas; +obs_source: human | — |
| @Scoles2019-ug.md | modified | +type: paper; +citekey: Scoles2019-ug | diseases empty; study_type not inferred |
| @Senior2020-xn.md | modified | +type: paper; +citekey: Senior2020-xn; +n_total: 170 | diseases empty; study_type not inferred |
| @Serrano-Pozo2021-ft.md | modified | +type: paper; +citekey: Serrano-Pozo2021-ft; +diseases: 1; +genes: 1; +study_type: review; +obs_source: human | — |
| @Sevigny2016-yi.md | modified | +type: paper; +citekey: Sevigny2016-yi; +diseases: 1; +study_type: clinical-trial | — |
| @Shearer1999-fw.md | modified | +type: paper; +citekey: Shearer1999-fw; +genes: 1; +study_type: exome | diseases empty |
| @Shen2020-yf.md | modified | +type: paper; +citekey: Shen2020-yf | diseases empty; study_type not inferred |
| @Shen2024-va.md | modified | +type: paper; +citekey: Shen2024-va; +diseases: 1; +study_type: exome | — |
| @Sherva2020-uj.md | modified | +type: paper; +citekey: Sherva2020-uj; +diseases: 1; +study_type: gwas; +obs_source: human | — |
| @Shojima2023-xm.md | modified | +type: paper; +citekey: Shojima2023-xm; +diseases: 2; +study_type: gwas | — |
| @Sierksma2020-xx.md | modified | +type: paper; +citekey: Sierksma2020-xx | diseases empty; study_type not inferred |
| @Significant Figures.md | modified | +type: paper; +citekey: Significant Figures | diseases empty; study_type not inferred |
| @Silberstein2009-le.md | modified | +type: paper; +citekey: Silberstein2009-le | diseases empty; study_type not inferred |
| @Simon2022-ab.md | modified | +type: paper; +citekey: Simon2022-ab; +diseases: 1 | study_type not inferred |
| @Simone2021-wk.md | modified | +type: paper; +citekey: Simone2021-wk | diseases empty; study_type not inferred |
| @Simren2022-tj.md | modified | +type: paper; +citekey: Simren2022-tj; +diseases: 1; +obs_source: human | study_type not inferred |
| @Singh2022-ol.md | modified | +type: paper; +citekey: Singh2022-ol; +diseases: 2; +genes: 2; +study_type: exome | — |
| @Skinner2014-pv.md | modified | +type: paper; +citekey: Skinner2014-pv; +study_type: clinical-trial | diseases empty |
| @Skotte2014-gh.md | modified | +type: paper; +citekey: Skotte2014-gh | diseases empty; study_type not inferred |
| @Sleegers2015-bj.md | modified | +type: paper; +citekey: Sleegers2015-bj; +diseases: 1; +n_total: 2181; +obs_source: human | study_type not inferred |
| @Sliter2018-zi.md | modified | +type: paper; +citekey: Sliter2018-zi; +diseases: 1 | study_type not inferred |
| @Sloan-Heggen2016-wh.md | modified | +type: paper; +citekey: Sloan-Heggen2016-wh; +genes: 4; +n_total: 408 | diseases empty; study_type not inferred |
| @Smith2022-it.md | modified | +type: paper; +citekey: Smith2022-it; +diseases: 1; +obs_source: human | study_type not inferred |
| @Song2018-zj.md | modified | +type: paper; +citekey: Song2018-zj; +diseases: 1; +study_type: review | — |
| @Southgate2020-al.md | modified | +type: paper; +citekey: Southgate2020-al; +diseases: 1 | study_type not inferred |
| @Sperling2020-wm.md | modified | +type: paper; +citekey: Sperling2020-wm; +diseases: 1; +obs_source: human | study_type not inferred |
| @Srinivasan2020-px.md | modified | +type: paper; +citekey: Srinivasan2020-px; +diseases: 1; +study_type: functional; +n_total: 10; +obs_source: human | — |
| @Stalin Breaker of Nations.md | modified | +type: paper; +citekey: Stalin Breaker of Nations | diseases empty; study_type not inferred |
| @Stevenson-Hoare2022-dl.md | modified | +type: paper; +citekey: Stevenson-Hoare2022-dl; +diseases: 1 | study_type not inferred |
| @Stewart2014-hz.md | modified | +type: paper; +citekey: Stewart2014-hz | diseases empty; study_type not inferred |
| @Stewart2018-ej.md | modified | +type: paper; +citekey: Stewart2018-ej | diseases empty; study_type not inferred |
| @Stockwell2023-hd.md | modified | +type: paper; +citekey: Stockwell2023-hd; +diseases: 1; +study_type: gwas; +n_total: 7105 | — |
| @Strain2020-qf.md | modified | +type: paper; +citekey: Strain2020-qf; +study_type: meta-analysis; +obs_source: human | diseases empty |
| @Stricker2020-hb.md | modified | +type: paper; +citekey: Stricker2020-hb; +diseases: 1; +n_total: 33 | study_type not inferred |
| @Stricker2020-qg.md | modified | +type: paper; +citekey: Stricker2020-qg; +diseases: 1; +study_type: review; +obs_source: human | — |
| @Suarez-Calvet2016-pd.md | modified | +type: paper; +citekey: Suarez-Calvet2016-pd; +diseases: 1 | study_type not inferred |
| @Sudlow2015-cs.md | modified | +type: paper; +citekey: Sudlow2015-cs; +diseases: 2; +obs_source: human | study_type not inferred |
| @Suh2006-mm.md | modified | +type: paper; +citekey: Suh2006-mm; +study_type: review; +obs_source: human | diseases empty |
| @Sun2020-yb.md | modified | +type: paper; +citekey: Sun2020-yb; +diseases: 1 | study_type not inferred |
| @Suzuki2020-iv.md | modified | +type: paper; +citekey: Suzuki2020-iv; +diseases: 1; +genes: 1; +obs_source: human | study_type not inferred |
| @Svoboda2019-ld.md | modified | +type: paper; +citekey: Svoboda2019-ld; +obs_source: human | diseases empty; study_type not inferred |
| @THe Biggest Ideas in the Universe.md | modified | +type: paper; +citekey: THe Biggest Ideas in the Universe | diseases empty; study_type not inferred |
| @Tabrizi2019-jz.md | modified | +type: paper; +citekey: Tabrizi2019-jz; +diseases: 1; +study_type: clinical-trial | — |
| @Tabrizi2020-op 1.md | modified | +type: paper; +citekey: Tabrizi2020-op 1 | diseases empty; study_type not inferred |
| @Tabrizi2020-op.md | modified | +type: paper; +citekey: Tabrizi2020-op; +diseases: 1; +study_type: functional; +n_total: 100000 | — |
| @Tabrizi2022-ql.md | modified | +type: paper; +citekey: Tabrizi2022-ql; +diseases: 1 | study_type not inferred |
| @Tai2023-nq.md | modified | +type: paper; +citekey: Tai2023-nq | diseases empty; study_type not inferred |
| @Tang2019-zi.md | modified | +type: paper; +citekey: Tang2019-zi; +study_type: gwas; +obs_source: human | diseases empty |
| @Tanigawa2020-lo.md | modified | +type: paper; +citekey: Tanigawa2020-lo; +diseases: 1; +genes: 1 | study_type not inferred |
| @Tank2021-lh.md | modified | +type: paper; +citekey: Tank2021-lh; +diseases: 1; +genes: 1; +study_type: gwas; +obs_source: human | — |
| @Tanna2018-yn.md | modified | +type: paper; +citekey: Tanna2018-yn; +diseases: 1 | study_type not inferred |
| @Tao2016-xa.md | modified | +type: paper; +citekey: Tao2016-xa | diseases empty; study_type not inferred |
| @Taymans2016-qq.md | modified | +type: paper; +citekey: Taymans2016-qq; +diseases: 1 | study_type not inferred |
| @Tedja2018-ry.md | modified | +type: paper; +citekey: Tedja2018-ry | diseases empty; study_type not inferred |
| @Terstappen2021-gc.md | modified | +type: paper; +citekey: Terstappen2021-gc; +genes: 2; +study_type: review | diseases empty |
| @The Big Picture.md | modified | +type: paper; +citekey: The Big Picture; +study_type: exome | diseases empty |
| @The Borgias Power and Fortune.md | modified | +type: paper; +citekey: The Borgias Power and Fortune | diseases empty; study_type not inferred |
| @The Brothers Karamazov.md | modified | +type: paper; +citekey: The Brothers Karamazov; +study_type: exome | diseases empty |
| @The Conquering Tide.md | modified | +type: paper; +citekey: The Conquering Tide | diseases empty; study_type not inferred |
| @The Courage to Be Disliked.md | modified | +type: paper; +citekey: The Courage to Be Disliked | diseases empty; study_type not inferred |
| @The Courage to Be Happy.md | modified | +type: paper; +citekey: The Courage to Be Happy | diseases empty; study_type not inferred |
| @The Gates of Europe.md | modified | +type: paper; +citekey: The Gates of Europe; +study_type: exome | diseases empty |
| @The Great Gasby.md | modified | +type: paper; +citekey: The Great Gasby | diseases empty; study_type not inferred |
| @The Idiot.md | modified | +type: paper; +citekey: The Idiot | diseases empty; study_type not inferred |
| @The Invention of Miracles – Language, Power, and Alexander Graham Bell's Quest to End Deafness.md | modified | +type: paper; +citekey: The Invention of Miracles – Language, Power, and Alexander Graham Bell's Quest to End Deafness | diseases empty; study_type not inferred |
| @The Making of the Atomic Bomb.md | modified | +type: paper; +citekey: The Making of the Atomic Bomb | diseases empty; study_type not inferred |
| @The Man from the Future.md | modified | +type: paper; +citekey: The Man from the Future | diseases empty; study_type not inferred |
| @The Medici.md | modified | +type: paper; +citekey: The Medici | diseases empty; study_type not inferred |
| @The Neurotic Character.md | modified | +type: paper; +citekey: The Neurotic Character | diseases empty; study_type not inferred |
| @The Power Broker.md | modified | +type: paper; +citekey: The Power Broker | diseases empty; study_type not inferred |
| @The River of Doubt.md | modified | +type: paper; +citekey: The River of Doubt | diseases empty; study_type not inferred |
| @The Sound and the Fury.md | modified | +type: paper; +citekey: The Sound and the Fury | diseases empty; study_type not inferred |
| @The Teenage Brain.md | modified | +type: paper; +citekey: The Teenage Brain | diseases empty; study_type not inferred |
| @Therriault2020-ry.md | modified | +type: paper; +citekey: Therriault2020-ry | diseases empty; study_type not inferred |
| @Therriault2024-wu.md | modified | +type: paper; +citekey: Therriault2024-wu; +diseases: 1; +study_type: review; +obs_source: human | — |
| @Thijssen2020-lo.md | modified | +type: paper; +citekey: Thijssen2020-lo; +diseases: 1 | study_type not inferred |
| @Thinakaran2008-qs.md | modified | +type: paper; +citekey: Thinakaran2008-qs | diseases empty; study_type not inferred |
| @Think Again.md | modified | +type: paper; +citekey: Think Again | diseases empty; study_type not inferred |
| @Thorgeirsson2008-ln.md | modified | +type: paper; +citekey: Thorgeirsson2008-ln | diseases empty; study_type not inferred |
| @Thorgeirsson2010-ym.md | modified | +type: paper; +citekey: Thorgeirsson2010-ym; +study_type: gwas; +n_total: 31266 | diseases empty |
| @Tian2021-tm.md | modified | +type: paper; +citekey: Tian2021-tm; +diseases: 2; +study_type: gwas | — |
| @Toden2020-be.md | modified | +type: paper; +citekey: Toden2020-be; +diseases: 1; +study_type: review | — |
| @Tolar2020-jg.md | modified | +type: paper; +citekey: Tolar2020-jg; +diseases: 1 | study_type not inferred |
| @Tolosa2020-st.md | modified | +type: paper; +citekey: Tolosa2020-st; +diseases: 1; +genes: 1; +study_type: clinical-trial | — |
| @Tools of Titans.md | modified | +type: paper; +citekey: Tools of Titans | diseases empty; study_type not inferred |
| @Toomey2018-qm.md | modified | +type: paper; +citekey: Toomey2018-qm; +diseases: 1; +genes: 2; +study_type: exome | — |
| @Tosto2017-qd.md | modified | +type: paper; +citekey: Tosto2017-qd; +diseases: 1; +n_total: 4792; +obs_source: human | study_type not inferred |
| @Tremblay-Mercier2021-nj.md | modified | +type: paper; +citekey: Tremblay-Mercier2021-nj | diseases empty; study_type not inferred |
| @Tribe of Mentors.md | modified | +type: paper; +citekey: Tribe of Mentors; +study_type: review | diseases empty |
| @Tropitzsch2023-gf.md | modified | +type: paper; +citekey: Tropitzsch2023-gf | diseases empty; study_type not inferred |
| @Trubetskoy2022-hx.md | modified | +type: paper; +citekey: Trubetskoy2022-hx; +diseases: 2; +study_type: gwas; +n_total: 76755 | — |
| @Twilight of the Gods.md | modified | +type: paper; +citekey: Twilight of the Gods | diseases empty; study_type not inferred |
| @Tziortzouda2021-dv.md | modified | +type: paper; +citekey: Tziortzouda2021-dv; +genes: 1 | diseases empty; study_type not inferred |
| @Tzoumas2022-lp.md | modified | +type: paper; +citekey: Tzoumas2022-lp; +diseases: 1; +genes: 1 | study_type not inferred |
| @Ulland2018-oc.md | modified | +type: paper; +citekey: Ulland2018-oc | diseases empty; study_type not inferred |
| @Usami2022-vf.md | modified | +type: paper; +citekey: Usami2022-vf; +genes: 1; +study_type: review | diseases empty |
| @Utermann1987-ar.md | modified | +type: paper; +citekey: Utermann1987-ar; +obs_source: human | diseases empty; study_type not inferred |
| @Vaci2020-qu.md | modified | +type: paper; +citekey: Vaci2020-qu; +diseases: 1; +n_total: 7415 | study_type not inferred |
| @Van_Dyck2022-au.md | modified | +type: paper; +citekey: Van_Dyck2022-au; +diseases: 1 | study_type not inferred |
| @Van_Harten2018-wk.md | modified | +type: paper; +citekey: Van_Harten2018-wk; +diseases: 1; +genes: 1 | study_type not inferred |
| @Van_Maurik2017-fv.md | modified | +type: paper; +citekey: Van_Maurik2017-fv; +diseases: 2 | study_type not inferred |
| @Van_Maurik2019-mt.md | modified | +type: paper; +citekey: Van_Maurik2019-mt; +diseases: 1 | study_type not inferred |
| @Van_Rheenen2021-eh.md | modified | +type: paper; +citekey: Van_Rheenen2021-eh; +genes: 1; +n_total: 8953; +obs_source: human | — |
| @Van_Swieten2008-rh.md | modified | +type: paper; +citekey: Van_Swieten2008-rh | diseases empty; study_type not inferred |
| @Van_der_Flier2008-ff.md | modified | +type: paper; +citekey: Van_der_Flier2008-ff | diseases empty; study_type not inferred |
| @Van_der_Mei2016-ye.md | modified | +type: paper; +citekey: Van_der_Mei2016-ye; +diseases: 1 | study_type not inferred |
| @Van_der_Poel2019-db.md | modified | +type: paper; +citekey: Van_der_Poel2019-db; +diseases: 1; +genes: 2; +obs_source: human | study_type not inferred |
| @Venegas2017-qk.md | modified | +type: paper; +citekey: Venegas2017-qk | diseases empty; study_type not inferred |
| @Venema2021-ui.md | modified | +type: paper; +citekey: Venema2021-ui | diseases empty; study_type not inferred |
| @Verberk2021-bp.md | modified | +type: paper; +citekey: Verberk2021-bp | diseases empty; study_type not inferred |
| @Verghese2011-pa.md | modified | +type: paper; +citekey: Verghese2011-pa | diseases empty; study_type not inferred |
| @Vermunt2022-gx.md | modified | +type: paper; +citekey: Vermunt2022-gx; +diseases: 1; +n_total: 1698 | study_type not inferred |
| @Verrelli2004-hj.md | modified | +type: paper; +citekey: Verrelli2004-hj | diseases empty; study_type not inferred |
| @Vincent-Viry1998-os.md | modified | +type: paper; +citekey: Vincent-Viry1998-os; +study_type: exome | diseases empty |
| @Vos2015-zp.md | modified | +type: paper; +citekey: Vos2015-zp | diseases empty; study_type not inferred |
| @Wallin2019-xh.md | modified | +type: paper; +citekey: Wallin2019-xh | diseases empty; study_type not inferred |
| @Wang2012-kq.md | modified | +type: paper; +citekey: Wang2012-kq; +genes: 2; +study_type: gwas | diseases empty |
| @Wang2019-za.md | modified | +type: paper; +citekey: Wang2019-za; +diseases: 1; +genes: 1; +study_type: review | — |
| @Wang2020-iy.md | modified | +type: paper; +citekey: Wang2020-iy; +diseases: 1 | study_type not inferred |
| @Wang2020-vr.md | modified | +type: paper; +citekey: Wang2020-vr; +diseases: 1; +genes: 1; +study_type: clinical-trial | — |
| @Warby2009-wb.md | modified | +type: paper; +citekey: Warby2009-wb; +diseases: 1 | study_type not inferred |
| @Ward2012-ic.md | modified | +type: paper; +citekey: Ward2012-ic; +diseases: 1; +study_type: review | — |
| @Wardell1987-ib.md | modified | +type: paper; +citekey: Wardell1987-ib; +diseases: 1; +genes: 1 | study_type not inferred |
| @Ware2015-tg.md | modified | +type: paper; +citekey: Ware2015-tg; +study_type: functional | diseases empty |
| @Watson2019-oc.md | modified | +type: paper; +citekey: Watson2019-oc; +study_type: gwas | diseases empty |
| @Weinreb2014-jv.md | modified | +type: paper; +citekey: Weinreb2014-jv; +diseases: 1; +study_type: review | — |
| @Weiss2008-zc.md | modified | +type: paper; +citekey: Weiss2008-zc; +obs_source: human | diseases empty; study_type not inferred |
| @Wells2019-lp.md | modified | +type: paper; +citekey: Wells2019-lp; +study_type: gwas | diseases empty |
| @Whiffin2020-um.md | modified | +type: paper; +citekey: Whiffin2020-um | diseases empty; study_type not inferred |
| @Whitwell2021-ow.md | modified | +type: paper; +citekey: Whitwell2021-ow; +diseases: 1; +obs_source: human | study_type not inferred |
| @Wightman2021-je.md | modified | +type: paper; +citekey: Wightman2021-je; +diseases: 2; +study_type: gwas; +n_total: 1126563 | — |
| @Wilfert2021-xj.md | modified | +type: paper; +citekey: Wilfert2021-xj; +diseases: 1 | study_type not inferred |
| @Williams2020-gk.md | modified | +type: paper; +citekey: Williams2020-gk; +diseases: 1 | study_type not inferred |
| @Willsey2022-nr.md | modified | +type: paper; +citekey: Willsey2022-nr; +diseases: 1 | study_type not inferred |
| @Wirtz2008-jx.md | modified | +type: paper; +citekey: Wirtz2008-jx; +diseases: 1; +genes: 1 | study_type not inferred |
| @Witkiewitz2019-xb.md | modified | +type: paper; +citekey: Witkiewitz2019-xb | diseases empty; study_type not inferred |
| @Wright2019-rl.md | modified | +type: paper; +citekey: Wright2019-rl; +diseases: 1 | study_type not inferred |
| @Wu2019-ze.md | modified | +type: paper; +citekey: Wu2019-ze | diseases empty; study_type not inferred |
| @Wu2022-qm.md | modified | +type: paper; +citekey: Wu2022-qm | diseases empty; study_type not inferred |
| @Xiong2021-gf.md | modified | +type: paper; +citekey: Xiong2021-gf; +genes: 1; +study_type: functional | diseases empty |
| @Xu2020-cq.md | modified | +type: paper; +citekey: Xu2020-cq; +study_type: gwas; +n_total: 286; +obs_source: human | diseases empty |
| @Xu2020-ms.md | modified | +type: paper; +citekey: Xu2020-ms; +genes: 1 | diseases empty; study_type not inferred |
| @Xu2021-kh.md | modified | +type: paper; +citekey: Xu2021-kh; +diseases: 1; +study_type: gwas; +obs_source: human | — |
| @Yamazaki2019-qk.md | modified | +type: paper; +citekey: Yamazaki2019-qk | diseases empty; study_type not inferred |
| @Yan2018-om.md | modified | +type: paper; +citekey: Yan2018-om | diseases empty; study_type not inferred |
| @Yang2023-fn.md | modified | +type: paper; +citekey: Yang2023-fn; +genes: 1; +study_type: functional; +obs_source: human | diseases empty |
| @Yeh2017-np.md | modified | +type: paper; +citekey: Yeh2017-np | diseases empty; study_type not inferred |
| @Yengo2018-le.md | modified | +type: paper; +citekey: Yengo2018-le; +study_type: gwas; +n_total: 700000 | diseases empty |
| @Yohrling2020-sh.md | modified | +type: paper; +citekey: Yohrling2020-sh | diseases empty; study_type not inferred |
| @Yokoyama2003-vb.md | modified | +type: paper; +citekey: Yokoyama2003-vb | diseases empty; study_type not inferred |
| @Young2021-aw.md | modified | +type: paper; +citekey: Young2021-aw; +genes: 10 | diseases empty; study_type not inferred |
| @Yu2020-sn.md | modified | +type: paper; +citekey: Yu2020-sn; +diseases: 1; +study_type: review | — |
| @Zahavi2015-rw.md | modified | +type: paper; +citekey: Zahavi2015-rw | diseases empty; study_type not inferred |
| @Zalocusky2021-qr.md | modified | +type: paper; +citekey: Zalocusky2021-qr | diseases empty; study_type not inferred |
| @Zannis1984-in.md | modified | +type: paper; +citekey: Zannis1984-in | diseases empty; study_type not inferred |
| @Zeitler2019-gy.md | modified | +type: paper; +citekey: Zeitler2019-gy | diseases empty; study_type not inferred |
| @Zeng2002-vb.md | modified | +type: paper; +citekey: Zeng2002-vb | diseases empty; study_type not inferred |
| @Zetterberg2020-fb.md | modified | +type: paper; +citekey: Zetterberg2020-fb; +diseases: 1 | study_type not inferred |
| @Zhang2018-li.md | modified | +type: paper; +citekey: Zhang2018-li; +study_type: gwas | diseases empty |
| @Zhang2020-qp.md | modified | +type: paper; +citekey: Zhang2020-qp; +genes: 2; +obs_source: human | diseases empty; study_type not inferred |
| @Zhang2020-qz.md | modified | +type: paper; +citekey: Zhang2020-qz; +diseases: 2; +study_type: gwas; +n_total: 11043; +obs_source: human | — |
| @Zhang2023-yo.md | modified | +type: paper; +citekey: Zhang2023-yo; +genes: 3; +n_total: 141456 | diseases empty; study_type not inferred |
| @Zhao2017-zt.md | modified | +type: paper; +citekey: Zhao2017-zt; +diseases: 1; +genes: 2; +study_type: exome; +obs_source: human | — |
| @Zhao2019-ro.md | modified | +type: paper; +citekey: Zhao2019-ro; +diseases: 1; +study_type: review | — |
| @Zhou2020-dk.md | modified | +type: paper; +citekey: Zhou2020-dk; +study_type: gwas; +n_total: 67589 | diseases empty |
| @Zhou2020-ko.md | modified | +type: paper; +citekey: Zhou2020-ko | diseases empty; study_type not inferred |
| @testing.md | modified | +type: paper; +citekey: testing | diseases empty; study_type not inferred |
| @van-der-Zwaan2025-et.md | modified | +type: paper; +citekey: van-der-Zwaan2025-et; +diseases: 1 | study_type not inferred |