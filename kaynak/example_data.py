"""Small deterministic computations used by the fictional teaching examples."""
import csv
import io
from collections import Counter
from decimal import Decimal


def summarize(source):
    rows=list(csv.DictReader(io.StringIO(source)))
    ids=[r['kayit_id'] for r in rows]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate registration ID')
    counts=Counter(r['durum'] for r in rows)
    missing=[r['kayit_id'] for r in rows if not r['tahsilat_tl'].strip()]
    total=sum((Decimal(r['tahsilat_tl'].replace('TL','').replace(',','.').strip())
               for r in rows if r['tahsilat_tl'].strip()), Decimal(0))
    unknown=[(r['kayit_id'],r['durum']) for r in rows if r['durum'] not in {'katıldı','iptal','bekliyor'}]
    return dict(rows=len(rows),counts=dict(counts),missing=missing,total=total,unknown=unknown)


def chart_csv(source):
    out=io.StringIO();writer=csv.writer(out,lineterminator='\n')
    writer.writerow(['durum','kayit_sayisi']);writer.writerows(summarize(source)['counts'].items())
    return out.getvalue()


def weekly_report(source):
    s=summarize(source)
    states='; '.join(f'{k}: {v}' for k,v in s['counts'].items())
    unknown='; '.join(f'{id}: {state}' for id,state in s['unknown']) or 'Yok'
    return (f'# İkinci hafta kayıt raporu\n\nKurgu veriye gerçek hesap uygulanmıştır. Bu dosya bir otomasyon veya skill çağrısının çalıştırma kaydı değildir.\n\n'
            f'- Kayıt sayısı: {s["rows"]}\n- Durumlar: {states}\n- Bilinen tahsilat: {s["total"]:,.0f} TL\n'
            f'- Eksik tahsilat: {", ".join(s["missing"]) or "Yok"}\n- Karar gerektiren yeni durum: {unknown}\n\n'
            'K08’in boş tutarı sıfırla doldurulmadı. K07’deki yedek durumu katıldı olarak eşlenmedi. K09 bekliyor olsa da 600 TL tahsilat toplamına dahil edildi; durum ile ödeme ayrı alanlardır.\n\n'
            'Kaynak: [katilim-hafta-2.csv](katilim-hafta-2.csv). Yöntem: [rapor-skill.md](rapor-skill.md).\n')
