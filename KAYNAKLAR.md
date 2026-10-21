# Kaynak ve kapsam denetimi

Tarih: 21 Ekim 2026. İçerik: 19 bölüm · 107 madde · 25 temel · 82 ileri.

Resmî OpenAI sayfalarının güncel birleşik kılavuzu indirilip ilgili bölümler okunmuştur. Aşağıdaki bağlantılar maddelerin dayanaklarını gösterir. Apple ve Git bağlantıları kendi platform belgeleridir.

Ürün davranışı, yerel CLI yardım doğrulaması ve editoryal öneri farklı kanıtlardır. Web sayfasının çalışması, örneklerdeki bütün Codex davranışlarının çalıştırıldığı anlamına gelmez.

| Kaynak | Bağlı maddeler |
|---|---|
| [Talimat katmanları](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 1.1, 1.2, 1.3, 1.4, 1.6, 18.1, 18.4, 19.3 |
| [Yapılandırma](https://learn.chatgpt.com/docs/config-file/config-reference) | 8.3 |
| [Config başlangıcı](https://learn.chatgpt.com/docs/config-file/config-basic) | 1.7, 5.4, 10.1, 19.4 |
| [CLI eğik çizgi komutları](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | 2.2, 2.3, 2.6, 2.7 |
| [CLI seçenekleri](https://learn.chatgpt.com/docs/cli/reference) | 6.1, 7.5, 12.6, 13.4 |
| [Alt ajanlar](https://learn.chatgpt.com/docs/agent-configuration/subagents) | 2.4, 5.1, 9.1, 11.6 |
| [Komut kuralları](https://learn.chatgpt.com/docs/agent-configuration/rules) | 6.2, 6.3 |
| [İzin profilleri · beta](https://learn.chatgpt.com/docs/permissions) | 6.6, 6.7, 7.1 |
| [Onaylar ve güvenlik](https://learn.chatgpt.com/docs/agent-approvals-security) | 7.2, 7.3, 7.4 |
| [Hook olayları](https://learn.chatgpt.com/docs/hooks) | 1.5, 7.6, 8.1, 8.2, 8.5, 8.6, 8.7 |
| [Skill geliştirme](https://learn.chatgpt.com/docs/build-skills) | 9.2, 9.3, 9.4 |
| [Plugin geliştirme](https://learn.chatgpt.com/docs/build-plugins) | 9.6, 10.3 |
| [Çalışma önerileri](https://learn.chatgpt.com/guides/best-practices) | 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 6.4, 6.5, 8.4, 10.2, 11.3, 11.4, 12.1, 12.2, 12.3, 12.4, 12.5, 13.1, 13.3, 13.5, 14.4, 15.1, 15.2, 15.3, 15.4, 16.1, 16.2, 16.3, 16.4, 17.2, 17.3, 18.3, 19.1, 19.5, 19.6 |
| [Projeler ve sohbetler](https://learn.chatgpt.com/docs/projects) | 2.1, 11.5, 18.2 |
| [Zamanlanmış görevler](https://learn.chatgpt.com/docs/automations) | 13.2, 14.1, 14.3, 14.5 |
| [Hız seçenekleri](https://learn.chatgpt.com/docs/agent-configuration/speed) | 5.5 |
| [Git worktree](https://git-scm.com/docs/git-worktree) | 11.1, 11.2, 19.2 |
| [Apple: simülatör ve cihaz](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices) | 17.1, 17.4, 17.5 |
| [Model ve düşünme seçimi](https://learn.chatgpt.com/docs/models) | 5.2, 5.3, 5.6 |
| [MCP bağlantıları](https://learn.chatgpt.com/docs/extend/mcp) | 9.5, 9.7 |
| [Etkileşimsiz kullanım](https://learn.chatgpt.com/docs/non-interactive-mode) | 14.2, 14.6 |

## Sınırlar

- CLI yardım kontrolü: 0.163.0-alpha.10.2 için sandbox, onay, exec JSONL/son mesaj/şema, review, MCP ve plugin komutlarının arayüzü.
- NOT_RUN: gerçek model karşılaştırması, tüm hook/izin senaryoları, zamanlanmış görev koşumları ve rehberdeki mobil örnekler.
- Sayfa işlevleri ve yayın kontrolü ayrı olarak [doğrulama raporunda](DOGRULAMA.md) kaydedilir.
