import Head from 'next/head'
import Image from 'next/image'
import NormalLayout from 'components/layouts/NormalLayout'
import OrderDetail from 'components/OrderDetail/OrderDetail'

export default function OrderDetailPage() {
    return (
        <OrderDetail />
    )
}


OrderDetailPage.getLayout = function getLayout(page) {
    return (
        <NormalLayout>
            {page}
        </NormalLayout>
    )
}